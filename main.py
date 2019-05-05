import random

class Dictionary:
	"""
	Emperors.txtを行ごとに読み取って_raw_dataに保存。
	_raw_dataをname,read,yearに分解し_emperors_listに保存。
	"""
	def __init__(self):
		with open("Emperors.txt", encoding="utf-8") as f:
			self._raw_data = [l for l in f.read().splitlines() if l]

		self._emperors_list = []
		for line in self._raw_data:
			print(line)
			name, read, year = line.split("\t")
			his_or_her_information = {"name": name, "read": read, "year": year}
			self._emperors_list.append(his_or_her_information)

AI = Dictionary()
print(AI._emperors_list)