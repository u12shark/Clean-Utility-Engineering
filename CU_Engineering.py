import streamlit as st

# 页面标题
st.set_page_config(page_title="工程计算工具箱", layout="wide")

st.title("🚀 欢迎使用工程计算工具箱")
st.markdown("""
这里集成了各类工程常用的计算模块，旨在提高工作效率。
            
### 👈 请从左侧边栏选择具体的计算模块
- **Valve Sizing**: 阀门选型计算
- **Pump Sizing**: 水泵选型计算（即将上线）
            
---
**版本说明：**
- v0.1: 初始化框架
- 开发者: [你的名字]
""")

st.info("提示：如果左侧没有看到菜单，请点击左上角的 '>' 按钮展开。")
