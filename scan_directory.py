#!/usr/bin/env python3
import os
import json
from pathlib import Path


def clean_module_name(name):
    """清理模块名称，去除 -graphify-out 后缀和尾部的 -"""
    # 去除 -graphify-out 后缀
    if name.endswith('-graphify-out'):
        name = name[:-12]
    
    # 去除尾部的 -
    if name.endswith('-'):
        name = name[:-1]
    
    return name


def is_graphify_module(dir_path):
    """检查目录是否是 graphify 模块"""
    # 方式1: 目录名以 -graphify-out 结尾
    if dir_path.name.endswith('-graphify-out'):
        return True
    
    # 方式2: 目录包含 graph.json 和 graph.html
    graph_json = dir_path / 'graph.json'
    graph_html = dir_path / 'graph.html'
    if graph_json.exists() and graph_html.exists():
        return True
    
    return False


def scan_directory(base_dir, parent_path=''):
    """递归扫描目录，构建树形结构"""
    items = []
    
    # 获取所有子项并排序
    children = []
    try:
        children = sorted(os.listdir(base_dir))
    except PermissionError:
        return items
    
    for item_name in children:
        # 跳过隐藏文件和脚本
        if item_name.startswith('.') or item_name in ['ANALYSIS_REPORT模板.md', 'scan_directory.py', 'generate_index.py', 'index.html', 'search_index.json', 'directory_tree.json']:
            continue
            
        item_path = base_dir / item_name
        if not item_path.is_dir():
            continue
        
        # 构建当前路径
        current_path = f"{parent_path}/{item_name}" if parent_path else item_name
        
        # 检查是否是 graphify 模块
        if is_graphify_module(item_path):
            module_info = parse_module(item_path, current_path)
            if module_info:
                items.append(module_info)
        else:
            # 这是分类目录，递归扫描
            category = {
                'type': 'category',
                'name': item_name,
                'display_name': clean_module_name(item_name),
                'path': current_path,
                'children': scan_directory(item_path, current_path)
            }
            # 只保留有子项的分类
            if category['children']:
                items.append(category)
    
    return items


def parse_module(module_path, current_path):
    """解析模块信息"""
    graph_json = module_path / 'graph.json'
    graph_html = module_path / 'graph.html'
    
    if not (graph_json.exists() and graph_html.exists()):
        return None
    
    # 读取统计信息
    num_nodes = 0
    num_edges = 0
    num_communities = 0
    
    try:
        with open(graph_json, 'r') as f:
            data = json.load(f)
            num_nodes = len(data.get('nodes', []))
            num_edges = len(data.get('links', []))
            
            # 计算社区数量
            communities = set()
            for node in data.get('nodes', []):
                community = node.get('community')
                if community is not None:
                    communities.add(community)
            num_communities = len(communities)
    except Exception as e:
        print(f"Error parsing {graph_json}: {e}")
        return None
    
    # 使用传入的完整路径
    module_name = module_path.name
    
    return {
        'type': 'module',
        'name': module_name,
        'display_name': clean_module_name(module_name),
        'path': current_path,
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'num_communities': num_communities,
        'graph_html': f"{current_path}/graph.html",
        'graph_report': f"{current_path}/GRAPH_REPORT.md",
        'analysis_report': f"{current_path}/ANALYSIS_REPORT.md"
    }


def count_stats(items):
    """统计模块数量和总数"""
    total_modules = 0
    total_nodes = 0
    total_edges = 0
    total_communities = 0
    
    for item in items:
        if item['type'] == 'module':
            total_modules += 1
            total_nodes += item['num_nodes']
            total_edges += item['num_edges']
            total_communities += item['num_communities']
        elif item['type'] == 'category' and item['children']:
            sub_stats = count_stats(item['children'])
            total_modules += sub_stats['modules']
            total_nodes += sub_stats['nodes']
            total_edges += sub_stats['edges']
            total_communities += sub_stats['communities']
    
    return {
        'modules': total_modules,
        'nodes': total_nodes,
        'edges': total_edges,
        'communities': total_communities
    }


def main():
    base_dir = Path(__file__).parent
    
    # 扫描目录
    directory_tree = scan_directory(base_dir)
    
    # 统计信息
    stats = count_stats(directory_tree)
    
    # 输出结果
    result = {
        'tree': directory_tree,
        'stats': stats
    }
    
    # 保存为 JSON
    with open(base_dir / 'directory_tree.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"Scanned {stats['modules']} modules with {stats['nodes']:,} nodes, {stats['edges']:,} edges, {stats['communities']:,} communities")
    print("Generated directory_tree.json")


if __name__ == '__main__':
    main()
