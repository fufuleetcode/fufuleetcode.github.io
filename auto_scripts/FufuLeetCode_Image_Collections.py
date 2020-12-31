import os 
from typing import List, Dict, Set, Tuple
import datetime
import shutil
import re
path_lc_io = "/Volumes/ZhentaoFiles-1/个人数据/【主播】/Leetcode讲解课程/"
image_output = "../images/posts/"
question_folder_template = "lc_*"



# STEP-1: file the list of question folders path
def list_folders(parent_folder:str, pattern:str) -> List[str]:
	res:List[str] = [x for x in os.listdir(parent_folder) if re.compile(pattern).match(x) and "." not in x]
	return sorted(res)



def generate_images():
	list_folder = list_folders(path_lc_io, question_folder_template)
	for folder in list_folder:
		source_path = os.path.join(path_lc_io, folder, folder)
		if not os.path.exists(source_path):
			print("Folder not found " + source_path + "!")
			continue

		target_path = os.path.join(image_output, "lc_"+folder.split("/")[-1].split("_")[1])

		overwrite_mode = True
		if os.path.exists(target_path) and not overwrite_mode:
			raise Exception("Folder exists!" + target_path)
		if not os.path.exists(target_path) :
			os.mkdir(target_path)
			print("Folder created: "+ target_path)

		for file_name in os.listdir(source_path):
			shutil.copy(os.path.join(source_path, file_name), os.path.join(target_path, file_name.lower().replace(".jpeg",".jpg")))
			print("copying" + os.path.join(source_path, file_name))


def generate_blog_md():
	import json

	blog_template_md_file = "./2020-01-01-lc-xxx.md"
	list_folder = list_folders(path_lc_io, question_folder_template)

	import pandas as pd
	meta_df  = pd.read_csv("./meta_summary.csv")
	
	for meta_dict in meta_df.to_dict('records'):
		
		print("====================================================================")
		import pprint
		meta_dict = {k:str(v).strip() for k,v in meta_dict.items() if str(v) not in { "nan" }}
		pprint.pprint(meta_dict)
		blog_md_file_content: str = open(blog_template_md_file, "r").read()

		# title {{blog_title}}
		lc_number = str(meta_dict.get("lc_number"))
		lc_question = str(meta_dict.get("lc_question"))
		blog_title = f"LeetCode {lc_number}. {lc_question} 解答"
		blog_md_file_content = blog_md_file_content.replace("""{{blog_title}}""", blog_title)
		
		# categories {{categories}}
		lc_difficulty = meta_dict.get("lc_difficulty", "")
		lc_tags = [i.strip() for i in meta_dict.get("lc_tags", "").split(",")]
		categories = "[难度 " + lc_difficulty + ", " + ", ".join(["主题 " + tag for tag in lc_tags]) + " ]"
		blog_md_file_content = blog_md_file_content.replace("""{{categories}}""", categories)


		# description {{description}}
		description = str( meta_dict.get("description", ""))
		blog_md_file_content = blog_md_file_content.replace("""{{description}}""", description)


		# keywords {{keywords}}
		keywords = [i.strip() for i in meta_dict.get("lc_tags", "").split(",")]
		keywords = ", ".join(keywords)
		blog_md_file_content = blog_md_file_content.replace("""{{keywords}}""", keywords)

		# youtube_video_link {{youtube_video_link}}
		youtube_video_number = meta_dict.get("youtube_video_number", "")
		blog_md_file_content = blog_md_file_content.replace("""{{youtube_video_number}}""", youtube_video_number)


		# bilibili_video_link {{bilibili_video_link}}
		bilibili_video_link = meta_dict.get("bilibili_video_link", "")
		blog_md_file_content = blog_md_file_content.replace("""{{bilibili_video_link}}""", bilibili_video_link)
		# blog_md_file_content = blog_md_file_content.replace("""{{bilibili_embed_video_link}}""", bilibili_video_link)

		# youtube_channel_link {{youtube_channel_link}}
		youtube_channel_link = "https://www.youtube.com/channel/UCCMpGENpr93ENbfdinP3QeQ"
		blog_md_file_content = blog_md_file_content.replace("""{{youtube_channel_link}}""", youtube_channel_link)

		# knowledge points 
		"""
			- [分治(Divide and Conquer)][]
			- [堆(Heap)][]
			- [排序(Sort)][]
		"""
		tag_translate = {
			"Array":"数组", 
			"Hash Table":"哈希表",
			"Array":"数组",
			"Linked List":"链表",
			"Math":"数学",
			"Two Pointers":"双指针",
			"String":"字符串",
			"Binary Search":"二分查找",
			"Divide and Conquer":"分治",
			"Dynamic Programming":"动态规划",
			"Backtracking":"回溯",
			"Stack":"栈",
			"Heap":"堆",
			"Greedy":"贪心算法",
			"Sort":"排序",
			"Tree":"树",
			"Depth-first Search":"深度优先搜索",
			"Breadth-first Search":"广度优先搜索",
			"Binary Search Tree":"二叉查找树",
			"Recursion":"递归",
			"Queue":"队列",
			"Sliding Window":"移动窗口"
		}
		knowledge_point = [i.strip() for i in meta_dict.get("lc_tags", "").split(",")]
		knowledge_point = [f"{tag_translate.get(i, '')}({i})" for i in knowledge_point]
		knowledge_point = "\n".join(["- [{}][]".format(kp) for kp in knowledge_point])
		blog_md_file_content = blog_md_file_content.replace("""{{knowledge_point}}""", knowledge_point)


		# ppt_images 
		"""
			- ![](/images/posts/lc_973/Slide1.jpeg)
			- ![](/images/posts/lc_973/Slide2.jpeg)
			- ![](/images/posts/lc_973/Slide3.jpeg)
			- ![](/images/posts/lc_973/Slide4.jpeg)
			- ![](/images/posts/lc_973/Slide5.jpeg)
			- ![](/images/posts/lc_973/Slide6.jpeg)
			- ![](/images/posts/lc_973/Slide7.jpeg)
		"""
		target_path = os.path.join(image_output, "lc_"+str(lc_number))
		image_names = []
		for file_name in sorted(os.listdir(target_path)):
			print(file_name)
			image_names.append(file_name)
		lc_number = meta_dict.get("lc_number","")
		ppt_images = "\n".join(["- ![](/images/posts/lc_{}/{})".format(lc_number, image_name) for image_name in image_names])
		blog_md_file_content = blog_md_file_content.replace("""{{ppt_images}}""", ppt_images)



		# {{github_code_link}}
		github_code_link = meta_dict.get("github_code_link","")
		blog_md_file_content = blog_md_file_content.replace("""{{github_code_link}}""", github_code_link)


		# {{python_code}}
		# convert from https://github.com/fufuleetcode/FufuLeetCode/blob/master/1.two-sum.py
		# to https://raw.githubusercontent.com/fufuleetcode/FufuLeetCode/master/1.two-sum.py
		python_code = ""
		try:
			github_raw_code_link = github_code_link.replace("https://github.com/fufuleetcode/FufuLeetCode/blob", "https://raw.githubusercontent.com/fufuleetcode/FufuLeetCode")
			# download code
			import urllib.request
			page = urllib.request.urlopen(github_raw_code_link)
			python_code =page.read().decode("utf-8") 
			#remove headers (before # @lc code=start)and tailers (after # @lc code=end)
			if "# @lc code=start" not in python_code or "# @lc code=end" not in python_code:
				print("Warning, # @lc code=end OR @lc code=start not found")
			# code cleaning
			python_code = python_code[python_code.find('class Solution'):]
			python_code = python_code[:python_code.find('# @lc code=end')]
			python_code = python_code.strip()
		except Exception:
			print("Warning! Error in fetching python code")
			python_code = ""
		blog_md_file_content = blog_md_file_content.replace("""{{python_code}}""", python_code)


		# save file
		date_start = datetime.datetime(2020, 1, 1)
		date = date_start - datetime.timedelta(days=int(lc_number))
		year,  month, day = date.year, date.month, date.day
		with open("../_posts/{}-{}-{}-lc-{}.md".format(year, month, day, lc_number),"w") as fh:
			fh.write(blog_md_file_content)



generate_images()
generate_blog_md()







