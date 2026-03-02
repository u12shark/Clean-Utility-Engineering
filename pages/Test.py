import streamlit as st

st.title("⚖️ 阀门选型计算 (Valve Sizing)")

# 输入区
with st.sidebar:
    st.header("输入参数")
    p1 = st.number_input("进口压力 P1 (bar)", value=10.0)
    p2 = st.number_input("出口压力 P2 (bar)", value=8.0)
    flow = st.number_input("流量 Q (m³/h)", value=100.0)

# 计算逻辑
pressure_drop = p1 - p2

# 输出区
st.subheader("计算结果")
if pressure_drop <= 0:
    st.error("错误：出口压力不能大于等于进口压力！")
else:
    st.metric("压力损失 (ΔP)", f"{pressure_drop:.2f} bar")
    st.write(f"当前的流量设定为: {flow} m³/h")
    # 这里以后可以放你更复杂的 Cv 值计算公式
