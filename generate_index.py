#!/usr/bin/env python3
import os
import json
from pathlib import Path

def main():
    base_dir = Path('/workspace/all-graphify-out')
    modules = []
    search_index = []
    
    # 定义类别颜色
    category_colors = {
        'admin': ('#667eea', '#764ba2'),  # 紫色渐变
        'examples': ('#f093fb', '#f5576c'),  # 粉色渐变
        'spring-boot-starters': ('#4facfe', '#00f2fe'),  # 蓝色渐变
        'agent-framework': ('#43e97b', '#38f9d7'),  # 绿色渐变
        'graph-core': ('#fa709a', '#fee140'),  # 橙色渐变
        'sandbox': ('#a18cd1', '#fbc2eb'),  # 薰衣草渐变
        'studio': ('#f6d365', '#fda085'),  # 暖色渐变
    }
    
    # 模块中文含义映射
    module_chinese_names = {
        'agentscope': 'AgentScope 智能代理框架',
        'chatbot': '聊天机器人示例',
        'deepresearch': '深度研究助手',
        'documentation': '文档问答示例',
        'multiagent-patterns': '多代理协作模式',
        'multimodal': '多模态交互示例',
        'voice-agent': '语音代理应用',
        'spring-ai-alibaba-admin-server-core': '管理员核心服务',
        'spring-ai-alibaba-admin-server-openapi': 'OpenAPI 网关接口',
        'spring-ai-alibaba-admin-server-runtime': '运行时管理服务',
        'spring-ai-alibaba-admin-server-start': '启动与前端服务',
        'spring-ai-alibaba-agent-framework': 'AI 代理框架核心',
        'spring-ai-alibaba-graph-core': '知识图谱引擎',
        'spring-ai-alibaba-sandbox': '沙箱执行环境',
        'spring-ai-alibaba-studio': 'AI 应用工作室',
    }
    
    # Scan directories recursively
    for dirpath, dirnames, filenames in os.walk(base_dir):
        dirpath = Path(dirpath)
        if 'graph.json' in filenames and 'GRAPH_REPORT.md' in filenames:
            # Skip cache directories
            if dirpath.name == 'cache':
                continue
                
            # Parse module name
            rel_path = dirpath.relative_to(base_dir)
            parts = list(rel_path.parts)
            
            module_name = dirpath.name
            if module_name.endswith('-graphify-out'):
                module_name = module_name[:-12]  # Remove -graphify-out suffix
                
            category = 'other'
            for cat in category_colors.keys():
                if cat in str(rel_path):
                    category = cat
                    break
            
            # Load graph.json
            try:
                with open(dirpath / 'graph.json', 'r') as f:
                    graph_data = json.load(f)
                
                num_nodes = len(graph_data.get('nodes', []))
                num_edges = len(graph_data.get('links', []))
                
                # Count communities
                communities = set()
                for node in graph_data.get('nodes', []):
                    if 'community' in node:
                        communities.add(node['community'])
                num_communities = len(communities)
                
                # Collect nodes for search index
                for node in graph_data.get('nodes', []):
                    search_index.append({
                        'module': module_name,
                        'module_path': str(rel_path),
                        'node_label': node.get('label', ''),
                        'node_id': node.get('id', ''),
                        'file_type': node.get('file_type', ''),
                        'source_file': node.get('source_file', ''),
                    })
                
            except Exception as e:
                num_nodes = 0
                num_edges = 0
                num_communities = 0
                print(f"Error loading {dirpath / 'graph.json'}: {e}")
            
            # Read GRAPH_REPORT.md for summary
            report_path = dirpath / 'GRAPH_REPORT.md'
            summary_text = ''
            try:
                with open(report_path, 'r') as f:
                    for i, line in enumerate(f):
                        if i > 20:  # Read first 20 lines
                            break
                        summary_text += line
            except Exception as e:
                print(f"Error loading {report_path}: {e}")
            
            # Get relative URL paths
            graph_html_url = str(rel_path / 'graph.html')
            report_url = str(rel_path / 'GRAPH_REPORT.md')
            analysis_url = str(rel_path / 'ANALYSIS_REPORT.md')
            
            # Check if analysis report exists
            has_analysis = (dirpath / 'ANALYSIS_REPORT.md').exists()
            
            modules.append({
                'name': module_name,
                'category': category,
                'path': str(rel_path),
                'num_nodes': num_nodes,
                'num_edges': num_edges,
                'num_communities': num_communities,
                'graph_html_url': graph_html_url,
                'report_url': report_url,
                'analysis_url': analysis_url if has_analysis else None,
                'summary': summary_text,
            })
    
    # Sort modules by name
    modules.sort(key=lambda m: m['name'])
    
    # Write search_index.json
    search_index_path = base_dir / 'search_index.json'
    with open(search_index_path, 'w') as f:
        json.dump({
            'modules': modules,
            'nodes': search_index,
        }, f, indent=2)
    
    print(f"Generated search_index.json with {len(modules)} modules, {len(search_index)} nodes")
    
    # Write index.html
    generate_index_html(base_dir, modules, category_colors, module_chinese_names)
    print("Generated index.html")

def generate_index_html(base_dir, modules, category_colors, module_chinese_names):
    # 类别中文名称映射
    category_chinese_names = {
        'admin': '管理后台',
        'examples': '示例项目',
        'spring-boot-starters': 'Spring Boot 启动器',
        'agent-framework': '代理框架',
        'graph-core': '图谱核心',
        'sandbox': '沙箱环境',
        'studio': '应用工作室',
        'other': '其他',
    }
    
    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spring AI Alibaba - 知识图谱索引</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            margin-bottom: 50px;
            color: white;
        }}
        
        header h1 {{
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        header p {{
            font-size: 1.1rem;
            opacity: 0.95;
            margin-bottom: 10px;
        }}
        
        .stats-bar {{
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
            margin-top: 30px;
        }}
        
        .stat-item {{
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            padding: 15px 25px;
            border-radius: 12px;
        }}
        
        .stat-value {{
            font-size: 2rem;
            font-weight: 700;
        }}
        
        .stat-label {{
            font-size: 0.9rem;
            opacity: 0.9;
        }}
        
        .search-container {{
            margin-bottom: 40px;
        }}
        
        #search {{
            width: 100%;
            max-width: 700px;
            display: block;
            margin: 0 auto;
            padding: 18px 24px;
            font-size: 1rem;
            border: none;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            outline: none;
        }}
        
        #search:focus {{
            box-shadow: 0 10px 60px rgba(0,0,0,0.3);
        }}
        
        .category-filter {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }}
        
        .filter-btn {{
            background: rgba(255,255,255,0.2);
            border: 2px solid rgba(255,255,255,0.4);
            color: white;
            padding: 10px 22px;
            border-radius: 30px;
            cursor: pointer;
            font-size: 0.95rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .filter-btn:hover, .filter-btn.active {{
            background: white;
            color: #667eea;
            border-color: white;
        }}
        
        .modules-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 28px;
        }}
        
        .module-card {{
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
        }}
        
        .module-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.2);
        }}
        
        .card-header {{
            padding: 24px;
            color: white;
            position: relative;
            overflow: hidden;
        }}
        
        .card-header::after {{
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        }}
        
        .category-badge {{
            display: inline-block;
            background: rgba(0,0,0,0.2);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }}
        
        .card-header h2 {{
            font-size: 1.4rem;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }}
        
        .module-chinese-name {{
            font-size: 0.9rem;
            opacity: 0.9;
            margin-top: 8px;
            font-weight: normal;
        }}
        
        .card-body {{
            padding: 24px;
        }}
        
        .card-stats {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }}
        
        .stat-card {{
            background: #f5f7fb;
            padding: 14px 10px;
            border-radius: 12px;
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 1.6rem;
            font-weight: 700;
            color: #667eea;
        }}
        
        .stat-desc {{
            font-size: 0.75rem;
            color: #888;
            margin-top: 4px;
            text-transform: uppercase;
        }}
        
        .card-actions {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        
        .btn {{
            flex: 1;
            min-width: 120px;
            padding: 12px 16px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.2s ease;
            text-decoration: none;
            text-align: center;
            display: inline-block;
        }}
        
        .btn-primary {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        
        .btn-primary:hover {{
            filter: brightness(1.1);
        }}
        
        .btn-secondary {{
            background: #f0f3fb;
            color: #444;
        }}
        
        .btn-secondary:hover {{
            background: #e5e9f5;
        }}
        
        .shortcuts {{
            margin-top: 50px;
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 16px;
            color: white;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .shortcuts h3 {{
            margin-bottom: 20px;
        }}
        
        .shortcuts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }}
        
        .shortcut-item {{
            display: flex;
            gap: 12px;
            align-items: center;
        }}
        
        .key {{
            background: rgba(0,0,0,0.3);
            padding: 4px 10px;
            border-radius: 6px;
            font-family: monospace;
            font-size: 0.9rem;
        }}
        
        footer {{
            text-align: center;
            color: white;
            margin-top: 60px;
            opacity: 0.8;
            font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2rem;
            }}
            
            .modules-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎨 Spring AI Alibaba - 知识图谱索引</h1>
            <p>Spring AI Alibaba 项目完整代码知识图谱可视化</p>
            <div class="stats-bar">
                <div class="stat-item">
                    <div class="stat-value">{len(modules)}</div>
                    <div class="stat-label">模块数量</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{sum(m['num_nodes'] for m in modules):,}</div>
                    <div class="stat-label">总节点数</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{sum(m['num_edges'] for m in modules):,}</div>
                    <div class="stat-label">总边数</div>
                </div>
            </div>
        </header>
        
        <div class="search-container">
            <input type="text" id="search" placeholder="🔍 搜索模块或节点... (Ctrl+K)">
        </div>
        
        <div class="category-filter">
            <button class="filter-btn active" data-filter="all">全部</button>
            {''.join([f'<button class="filter-btn" data-filter="{cat}">{category_chinese_names.get(cat, cat.title())}</button>' for cat in category_colors.keys()])}
        </div>
        
        <div class="modules-grid" id="modulesGrid">
            {generate_module_cards_cn(modules, category_colors, module_chinese_names)}
        </div>
        
        <div class="shortcuts">
            <h3>⌨️ 键盘快捷键</h3>
            <div class="shortcuts-grid">
                <div class="shortcut-item">
                    <span class="key">Ctrl+K</span>
                    <span>聚焦搜索框</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Ctrl+1</span>
                    <span>显示全部模块</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Ctrl+2</span>
                    <span>管理后台模块</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Ctrl+3</span>
                    <span>示例项目</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Ctrl+4</span>
                    <span>Spring Boot 启动器</span>
                </div>
            </div>
            <div style="margin-top:20px; padding-top:20px; border-top:1px solid rgba(255,255,255,0.2);">
                <p>💡 提示：点击任意卡片即可打开交互式知识图谱！</p>
            </div>
        </div>
        
        <footer>
            由 graphify 生成于 {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}
        </footer>
    </div>

    <script>
        // Load search index
        let searchIndex = null;
        fetch('search_index.json')
            .then(response => response.json())
            .then(data => {{
                searchIndex = data;
            }})
            .catch(err => console.error('Failed to load search index:', err));
        
        // Filter functionality
        const filterBtns = document.querySelectorAll('.filter-btn');
        const cards = document.querySelectorAll('.module-card');
        
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                const filter = btn.dataset.filter;
                
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                cards.forEach(card => {{
                    if (filter === 'all' || card.dataset.category === filter) {{
                        card.style.display = 'block';
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});
            }});
        }});
        
        // Search functionality
        const searchInput = document.getElementById('search');
        
        searchInput.addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase();
            
            cards.forEach(card => {{
                const name = card.querySelector('h2').textContent.toLowerCase();
                const category = card.dataset.category.toLowerCase();
                const chineseName = card.querySelector('.module-chinese-name')?.textContent.toLowerCase() || '';
                
                if (name.includes(query) || category.includes(query) || chineseName.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {{
            if (e.ctrlKey || e.metaKey) {{
                switch(e.key.toLowerCase()) {{
                    case 'k':
                        e.preventDefault();
                        searchInput.focus();
                        break;
                    case '1':
                        e.preventDefault();
                        filterBtns[0].click();
                        break;
                    case '2':
                        e.preventDefault();
                        const adminBtn = Array.from(filterBtns).find(b => b.dataset.filter === 'admin');
                        if (adminBtn) adminBtn.click();
                        break;
                    case '3':
                        e.preventDefault();
                        const examplesBtn = Array.from(filterBtns).find(b => b.dataset.filter === 'examples');
                        if (examplesBtn) examplesBtn.click();
                        break;
                    case '4':
                        e.preventDefault();
                        const startersBtn = Array.from(filterBtns).find(b => b.dataset.filter === 'spring-boot-starters');
                        if (startersBtn) startersBtn.click();
                        break;
                }}
            }}
        }});
    </script>
</body>
</html>'''
    
    with open(base_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_module_cards_cn(modules, category_colors, module_chinese_names):
    """生成中文模块卡片"""
    cards = []
    for module in modules:
        category = module['category']
        color1, color2 = category_colors.get(category, ('#667eea', '#764ba2'))
        
        # 去除模块名尾部的 '-'
        module_name = module['name']
        if module_name.endswith('-'):
            module_name = module_name[:-1]
        
        # 获取模块中文名称
        chinese_name = module_chinese_names.get(module_name, '')
        
        card_html = f'''
        <div class="module-card" data-category="{category}" onclick="window.open('{module['graph_html_url']}', '_blank')">
            <div class="card-header" style="background: linear-gradient(135deg, {color1} 0%, {color2} 100%);">
                <div class="category-badge">{category}</div>
                <h2>{module_name}</h2>
                {f'<div class="module-chinese-name">{chinese_name}</div>' if chinese_name else ''}
            </div>
            <div class="card-body">
                <div class="card-stats">
                    <div class="stat-card">
                        <div class="stat-number">{module['num_nodes']:,}</div>
                        <div class="stat-desc">节点</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{module['num_edges']:,}</div>
                        <div class="stat-desc">边</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{module['num_communities']}</div>
                        <div class="stat-desc">社区</div>
                    </div>
                </div>
                <div class="card-actions">
                    <a href="{module['graph_html_url']}" class="btn btn-primary" onclick="event.stopPropagation(); event.preventDefault(); window.open('{module['graph_html_url']}', '_blank');">📊 图谱</a>
                    <a href="{module['report_url']}" class="btn btn-secondary" onclick="event.stopPropagation(); event.preventDefault(); window.open('{module['report_url']}', '_blank');">📄 报告</a>
                    {f'<a href="{module["analysis_url"]}" class="btn btn-secondary" onclick="event.stopPropagation(); event.preventDefault(); window.open(\'{module["analysis_url"]}\', \'_blank\');">📑 分析</a>' if module['analysis_url'] else ''}
                </div>
            </div>
        </div>
        '''
        cards.append(card_html)
    
    return '\n'.join(cards)

def generate_module_cards(modules, category_colors):
    cards = []
    for module in modules:
        category = module['category']
        color1, color2 = category_colors.get(category, ('#667eea', '#764ba2'))
        
        # 去除模块名尾部的 '-'
        module_name = module['name']
        if module_name.endswith('-'):
            module_name = module_name[:-1]
        
        card_html = f'''
        <div class="module-card" data-category="{category}" onclick="window.open('{module['graph_html_url']}', '_blank')">
            <div class="card-header" style="background: linear-gradient(135deg, {color1} 0%, {color2} 100%);">
                <div class="category-badge">{category}</div>
                <h2>{module_name}</h2>
            </div>
            <div class="card-body">
                <div class="card-stats">
                    <div class="stat-card">
                        <div class="stat-number">{module['num_nodes']:,}</div>
                        <div class="stat-desc">Nodes</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{module['num_edges']:,}</div>
                        <div class="stat-desc">Edges</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{module['num_communities']}</div>
                        <div class="stat-desc">Communities</div>
                    </div>
                </div>
                <div class="card-actions">
                    <a href="{module['graph_html_url']}" class="btn btn-primary" onclick="event.stopPropagation(); event.preventDefault(); window.open('{module['graph_html_url']}', '_blank');">📊 Graph</a>
                    <a href="{module['report_url']}" class="btn btn-secondary" onclick="event.stopPropagation(); event.preventDefault(); window.open('{module['report_url']}', '_blank');">📄 Report</a>
                    {f'<a href="{module["analysis_url"]}" class="btn btn-secondary" onclick="event.stopPropagation(); event.preventDefault(); window.open(\'{module["analysis_url"]}\', \'_blank\');">📑 Analysis</a>' if module['analysis_url'] else ''}
                </div>
            </div>
        </div>
        '''
        cards.append(card_html)
    
    return '\n'.join(cards)

if __name__ == '__main__':
    main()
