from openai import OpenAI
# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key="sk-964bcad67d9d44e19e66d667b793825d", base_url="https://api.deepseek.com")

# startdate, enddate, time, theme,
def main(startdate, enddate, time, theme):

    date = f"学习计划的日期是从{startdate}到{enddate}。"
    dailytime = f"每天的{time}可以执行学习计划。"
    lessontheme = f"学习的主题是{theme}。"

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个私人学习助手，你将会收到一系列有关制定详细学习计划的信息，你将根据这些信息制定个性化的学习方案。"},
            {"role": "user", "content": """你制定学习计划遵循以下步骤：
                                            1.用户会先传输给你学习的主题，学习的日期和每天的最佳学习时间
                                            2.根据用户提供的学习主题搜索有关主题的详细学习内容，并列出内容列表，注意：学习内容一定要详细！要化成零碎的知识点然后分配
                                            3.根据用户提供的学习日期和每天最佳学习时间，将内容列表合理分配到时间安排中，但要留出一些调节时间，让用户既可以处理突发情况，又能按时完成任务
                                            4.将学习计划按照表格的格式输出，表格内要有学习的内容、学习的日期、每天的学习时间分配、学习内容的注意事项、学习时长的总和
                                            注意：你最后只需要输出学习计划的表格即可"""},
            {"role": "user", "content": lessontheme + date + dailytime},
      ],
        max_tokens=1024,
        temperature=0.7,
        stream=False
    )

    return response.choices[0].message.content