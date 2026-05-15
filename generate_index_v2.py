#!/usr/bin/env python3
import os
import json
from pathlib import Path


def scan_directory(base_dir):
    """扫描目录，构建目录树"""
    directory_tree = []
    
    # 扫描一级目录
    for item in sorted(os.listdir(base_dir)):
        item_path = base_dir / item
        if item_path.is_dir() and not item.startswith('.'):
            # 检查是否是 graphify-out 目录
            if item.endswith('-graphify-out'):
                # 这是一个模块
                module_info = parse_graphify_out(item_path, parent_path='')
                if module_info:
                    directory_tree.append(module_info)
            else:
                # 这是一个普通目录，继续递归扫描
                category_node = {
                    'type': 'category',
                    'name': item,
                    'display_name': item,
                    'path': str(item),
                    'children': []
                }
                # 递归扫描子目录
                scan_subdirectory(item_path, category_node['children'], str(item))
                if category_node['children']:  # 只保留有内容的分类
                    directory_tree.append(category_node)
    
    return directory_tree


def scan_subdirectory(dir_path, children, parent_path):
    """递归扫描子目录"""
    for item in sorted(os.listdir(dir_path)):
        item_path = dir_path / item
        if item_path.is_dir() and not item.startswith('.'):
            if item.endswith('-graphify-out'):
                # 这是一个模块
                module_info = parse_graphify_out(item_path, parent_path)
                if module_info:
                    children.append(module_info)
            else:
                # 这是一个子分类
                sub_category = {
                    'type': 'category',
                    'name': item,
                    'display_name': item,
                    'path': f"{parent_path}/{item}" if parent_path else item,
                    'children': []
                }
                scan_subdirectory(item_path, sub_category['children'], f"{parent_path}/{item}" if parent_path else item)
                if sub_category['children']:  # 只保留有内容的分类
                    children.append(sub_category)


def parse_graphify_out(dir_path, parent_path):
    """解析 graphify-out 目录，提取信息"""
    graph_json = dir_path / 'graph.json'
    graph_html = dir_path / 'graph.html'
    graph_report = dir_path / 'GRAPH_REPORT.md'
    analysis_report = dir_path / 'ANALYSIS_REPORT.md'
    
    if not (graph_json.exists() and graph_html.exists()):
        return None
    
    # 读取 graph.json 获取统计信息
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
    
    # 模块名称
    module_name = dir_path.name
    # 去除 -graphify-out 后缀
    if module_name.endswith('-graphify-out'):
        display_name = module_name[:-12]
    else:
        display_name = module_name
    # 确保没有尾部的 '-'
    if display_name.endswith('-'):
        display_name = display_name[:-1]
    
    return {
        'type': 'module',
        'name': module_name,
        'display_name': display_name,
        'path': f"{parent_path}/{module_name}" if parent_path else module_name,
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'num_communities': num_communities,
        'graph_html': f"{parent_path}/{module_name}/graph.html" if parent_path else f"{module_name}/graph.html",
        'graph_report': f"{parent_path}/{module_name}/GRAPH_REPORT.md" if parent_path else f"{module_name}/GRAPH_REPORT.md",
        'analysis_report': f"{parent_path}/{module_name}/ANALYSIS_REPORT.md" if parent_path else f"{module_name}/ANALYSIS_REPORT.md" if analysis_report.exists() else None
    }


def main():
    base_dir = Path(__file__).parent
    directory_tree = scan_directory(base_dir)
    
    # 保存目录树结构
    with open(base_dir / 'directory_tree.json', 'w', encoding='utf-8') as f:
        json.dump(directory_tree, f, ensure_ascii=False, indent=2)
    
    print(f"Generated directory_tree.json with {len(directory_tree)} top-level items")


if __name__ == '__main__':
    main()
