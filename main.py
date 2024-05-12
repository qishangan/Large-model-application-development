import streamlit as st
from PIL import Image
from utils import main

# 设置页面配置
st.set_page_config(page_title="学习计划生成", layout="wide")

# 加载公司logo
logo = Image.open("logo.png")


# 创建侧边栏并添加内容
st.sidebar.image(logo, use_column_width=True)
st.sidebar.header("项目简介")
st.sidebar.write("“梦织者”——我们选取这个名字，是因为我们相信教育是实现梦想的起点。我们的愿景是通过提供公平的教育机会，让每个人都能够编织并实现自己的梦想。")
st.sidebar.subheader("联系方式")
st.sidebar.write("电话: 15022690131")
st.sidebar.write("邮箱: 2307456103@qq.com")

# 应用的主要部分
st.title("📆学习计划生成")

theme = st.text_input("📖输入需要学习的课程名称")
date = st.text_input("📄输入学习计划的开始日期")
time = st.text_input("🕒输入每天有效的学习的时间")
list = st.text_input("🌟请输入课程目录")

submit = st.button("🔥生成计划")

if submit:
    with st.spinner("🚀学习计划正在生成中，请稍等...（大概两分钟左右）"):
        result = main(theme, list, time, date)
    st.success("学习计划已生成！")
    st.subheader("学习计划：")
    st.write(result)
