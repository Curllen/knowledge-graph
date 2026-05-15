# Knowledge Graph Navigator

代码知识图谱导航平台 - 动态浏览和管理 Graphify 生成的代码知识图谱。

## 功能特性

- 📁 **多级目录树导航** - 支持展开/折叠的分类目录结构
- ☑️ **级联选择** - 勾选父级自动选择所有子级模块
- 🔍 **实时搜索** - 支持按模块名、路径搜索 (快捷键: Ctrl+K)
- 🌓 **主题切换** - 支持深色/浅色模式
- 📊 **统计面板** - 实时显示模块、节点、边、社区数量
- 📄 **Markdown 弹窗** - 点击报告按钮在弹窗中查看详细分析

## 文件说明

### index.html
主页面文件，包含完整的 UI 和交互逻辑：
- 目录树渲染与级联选择
- 模块卡片展示
- 搜索过滤
- 主题切换
- Markdown 报告弹窗

### scan_directory.py
目录扫描脚本，用于生成导航数据：
- 递归扫描目录结构
- 识别 Graphify 模块（以 `-graphify-out` 结尾或包含 graph.json/graph.html）
- 提取模块统计信息（节点数、边数、社区数）
- 生成 `directory_tree.json` 数据文件

### directory_tree.json
扫描生成的数据文件，包含：
- 目录树结构（分类和模块）
- 模块统计信息
- 文件路径映射

### generate_index.py和generate_index_v2.py
- 已经无用了

## 快速开始

### 1. 生成目录数据

```bash
python3 scan_directory.py
```

运行后会扫描当前目录下的所有 Graphify 模块，生成 `directory_tree.json`。

### 2. 启动本地服务器

```bash
# Python 3
python3 -m http.server 8080

# 或使用 Node.js
npx serve .
```

### 3. 访问页面

打开浏览器访问 `http://localhost:8080`

## 使用说明

### 目录导航

- **展开/折叠**: 点击 ▶ 箭头展开或折叠子目录
- **选择模块**: 勾选复选框选择模块，父级勾选会自动选择所有子级
- **All Projects**: 点击按钮清除所有选择，显示全部模块

### 搜索功能

- 在搜索框输入关键词实时过滤模块
- 支持按模块名、路径搜索
- 快捷键 `Ctrl+K` 快速聚焦搜索框

### 查看报告

- **📊 图谱**: 在新标签页打开交互式知识图谱
- **📄 报告**: 在弹窗中查看 GRAPH_REPORT.md
- **📑 分析**: 在弹窗中查看 ANALYSIS_REPORT.md（如存在）

### 主题切换

点击右上角按钮切换深色/浅色主题，设置会自动保存到本地存储。

## 模块识别规则

脚本会自动识别以下类型的 Graphify 模块：

1. 目录名以 `-graphify-out` 结尾
2. 目录包含 `graph.json` 和 `graph.html` 文件

## 目录结构示例

```
all-graphify-out/
├── index.html              # 导航页面
├── scan_directory.py       # 扫描脚本
├── directory_tree.json     # 生成的数据文件
├── project-a-graphify-out/ # Graphify 模块
│   ├── graph.html
│   ├── graph.json
│   ├── GRAPH_REPORT.md
│   └── ANALYSIS_REPORT.md
├── project-b/              # 普通分类目录
│   └── sub-module-graphify-out/
└── README.md
```

## 技术栈

- **前端**: 原生 HTML5 + CSS3 + JavaScript
- **样式**: CSS 变量实现主题切换
- **Markdown 渲染**: Marked.js
- **后端**: Python 3 目录扫描

## 浏览器支持

- Chrome / Edge / Firefox / Safari 最新版本
- 支持移动端响应式布局

## 许可证

MIT License
