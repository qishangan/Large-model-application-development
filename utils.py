from openai import OpenAI
# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key="sk-964bcad67d9d44e19e66d667b793825d", base_url="https://api.deepseek.com")

# startdate, enddate, time, theme,
def main(theme, list, time, date):

    date = f"学习计划的开始日期：{date}。"
    dailytime = f"每天的有效学习时间大约：{time}。"
    lessontheme = f"学习的课程名称：{theme}。"
    lit = f"课程的目录：{list}。"

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个私人学习助手，你将会收到一系列有关制定详细学习计划的信息，你将根据这些信息制定个性化的学习方案。"},
            {"role": "user", "content": """你制定学习计划遵循以下步骤：
                                            1.用户会先传输给你需要学习的课程的名称和目录
                                            2.根据用户提供的课程名称和目录，评估每小节的课程难度，科学规划学习时间
                                            3.参考用户提供的每天有效学习时间和学习日期，将课程的内容合理地分配在每天的学习计划中，注意安排学习内容不是让你罗列课程目录，而是写清每天需要学习的课程小节
                                            日期格式：xx月xx日 ；学习内容格式 ：xx-xx集，{简写的课程小节标题} ；学习时长格式：xx分钟
                                            注意：你应该计算你分配的每天课程小节的总时长，每天学习总时长应小于等于有效学习时长，表格中的学习时长应等于包含课程小节的时长总和
                                            4.检查是否将课程目录的内容全部安排进学习计划中，检查是否有遗漏内容
                                            5.将学习计划按照表格的格式输出，表格内要有每天的学习内容、学习的日期、每天学习的时长
                                            注意：你的输出是表格，不是代码，不需要放入代码框中，也不需要button的按钮
                                            注意：最后输出完学习计划的表格后，可以说一些激励用户学习的话，帮助用户更有斗志地执行计划"""},
            {"role": "user", "content": lessontheme + dailytime + date + lit},
      ],
        max_tokens=29000,
        temperature=0.7,
        stream=False
    )

    return response.choices[0].message.content