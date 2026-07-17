<p align="center">
  <img src="五行图.png" width="120" alt="五行图" />
</p>

<h1 align="center">🀄️ 四柱八字命理 · AI 知识库</h1>

<p align="center">
  <strong>135 页、33 万字系统课程，让任何 AI 助手变身为命理学专家</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" /></a>
  <img src="https://img.shields.io/badge/页数-135-green.svg" alt="135 页" />
  <img src="https://img.shields.io/badge/知识库-33万字-orange.svg" alt="33 万字" />
  <img src="https://img.shields.io/badge/通用格式-全平台可用-purple.svg" alt="通用格式" />
</p>

<p align="center">
  <a href="#-cursor">Cursor</a> ·
  <a href="#-github-copilot">Copilot</a> ·
  <a href="#-claude-code">Claude Code</a> ·
  <a href="#-reasonix">Reasonix</a> ·
  <a href="#-chatgpt--claude--gemini--deepseek-等">ChatGPT</a> ·
  <a href="#-windsurf--continue--其它">更多…</a>
</p>

---

## 📖 这是什么？

一个**通用 AI 知识库**，内容来自 B站UP主 **易理施**（易学研究小组）的系统课程《四柱八字命理》。通过 OCR 数字化为 135 页、约 33 万字的全文知识库，覆盖从阴阳五行到格局大运的完整命理学体系。

> 💡 装上它，任何 AI 工具都能查阅这本"命理教科书"，引用原文回答四柱八字问题。

---

## 🎯 知识覆盖

<table>
<tr>
<td width="50%">

### 🔰 基础理论
- ☯️ 阴阳五行 · 天干地支
- 🌏 哲学基础（天道/地道/人道）
- 🌌 天文学依据（天体运行与气候变化）
- 📜 发展简史（伏羲 → 李虚中 → 徐子平）

### 🧩 核心体系
- 🎌 **日元** —— 四柱论命核心
- 🏷️ **十神** —— 正官·七杀·正印·偏印·食神·伤官·正财·偏财·比肩·劫财
- 🔗 **刑冲合害** —— 三合·六合·三会·六冲·三刑·六害

</td>
<td width="50%">

### 🏰 格局详解
- 正官格 · 七杀格
- 正印格 · 偏印格
- 食神格 · 伤官格
- 正财格 · 偏财格
- 建禄格 · 阳刃格

### 🔮 进阶应用
- 用神 · 喜神 · 忌神 · 调候
- 大运 · 流年推算
- 实战案例解析
- 健康信息分析

</td>
</tr>
</table>

---

## 📦 安装与使用

> **一招通用**：复制 [`prompt.md`](prompt.md) 的全部内容，粘贴到任何 AI 对话中即可激活。
>
> 下面各工具提供了更"原生"的集成方式。

### 🖱️ Cursor

```bash
git clone https://github.com/xhzair/sizhu_bazi.git
```

用 Cursor 打开项目目录即可 —— `.cursor/rules/sizhu-bazi.mdc` 已配好，AI 会在命理话题下自动查阅知识库。

### 🐙 GitHub Copilot

```bash
git clone https://github.com/xhzair/sizhu_bazi.git
```

用 VS Code（含 Copilot 插件）打开项目目录即可 —— `.github/copilot-instructions.md` 已配好。

### 💻 Claude Code

```bash
git clone https://github.com/xhzair/sizhu_bazi.git
cd sizhu_bazi && claude
```

直接对话，Claude Code 可自动读取 `prompt.md` 和知识库文件。

### 🧩 Reasonix

在 Reasonix 对话框中输入：

```
/install https://github.com/xhzair/sizhu_bazi
```

### 🌐 ChatGPT / Claude / Gemini / DeepSeek 等

1. 打开 [`prompt.md`](prompt.md)
2. 复制全部内容，粘贴到对话中
3. 上传 `sizhu-bazi/references/full_text.txt` 作为附件（或对话中指定路径）
4. 开始提问！

### 🌊 Windsurf / Continue / 其它

任何支持自定义规则或系统提示的 AI 工具，将 [`prompt.md`](prompt.md) 的内容设为系统级指令即可。如果工具支持读取项目文件，它会自动使用知识库。

---

## 🧪 效果演示

| 你问 | AI 回答 |
|------|---------|
| *"什么是日元？怎么判断强弱？"* | 查阅原文第20页起，引用原文详解答 |
| *"正官格和七杀格有什么区别？"* | 定位格局章节，逐条对比特征 |
| *"三合和六合有什么不同？"* | 搜索刑冲合害章节，给出精确定义 |
| *"帮我分析一个八字"* | 结合日主、十神、格局、用神综合分析 |

每次回答都会**引用原文**并标注**来源页码**。

---

## 📂 仓库结构

```
sizhu_bazi/
├── prompt.md                 ← 🌐 通用 Prompt（复制即用）
├── .cursor/rules/            ← 🖱️ Cursor 规则
│   └── sizhu-bazi.mdc
├── .github/
│   └── copilot-instructions.md ← 🐙 Copilot 指令
├── sizhu-bazi/               ← 🧩 Reasonix Skill 包
│   ├── SKILL.md
│   └── references/
│       └── full_text.txt     ← 📚 135页全文知识库（33万字）
├── sizhu-bazi.skill          ← 打包的 .skill 文件
├── ocr_output/               ← 逐页 OCR 文本（135页）
├── ocr_all.py                ← OCR 脚本（PyMuPDF + Tesseract）
├── tessdata/                 ← Tesseract 中文训练数据
├── 五行图.png                ← 五行生克图
├── 干支模型.png              ← 天干地支模型图
├── LICENSE                   ← MIT License
└── README.md
```

---

## ⚠️ 声明

- 内容来源于 B站UP主 **易理施**（易学研究小组）的公开课程，仅供学习研究使用
- 命理学是传统文化的一部分，请理性看待，**仅供娱乐参考**
- OCR 识别可能存在少量文字偏差，AI 使用时已做容错处理

---

## 🙏 致谢

- 课程作者：**易理施**（易学研究小组）
- OCR 引擎：[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- PDF 解析：[PyMuPDF](https://github.com/pymupdf/PyMuPDF)

---

<p align="center">
  <sub>🀄️ 通用 AI 知识库 · <a href="LICENSE">MIT License</a></sub>
</p>
