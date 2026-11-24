def caculator(graph):
	# damping factor (Google đề xuất và sử dụng phổ biến để mô phỏng hành vi người dùng khi duyệt web)
	# 85% khả năng: Người dùng tiếp tục nhấn vào một liên kết trên trang hiện tại để chuyển sang trang khác.
	# 15% khả năng: Người dùng không nhấn liên kết hiện tại mà chuyển ngẫu nhiên sang một trang khác.
	damping = 0.85
	epsilon = 0.000001
	max_iterations = 100000
	total_nodes = len(graph)
	iteration = 0

	degree = {key: len(value) for key, value in graph.items()}
	page_rank = dict.fromkeys(graph, 1)

	while iteration < max_iterations:
		new_page_rank = {}
		for key, value in graph.items():
			total = sum(page_rank[key]/degree[name] for name in value)

			new_page_rank[key] = ((1 - damping) / total_nodes + damping * total)
       		
		# Calculate error
		error = max(
			abs(new_page_rank[key] - page_rank[key])
			for key in graph
		)

		print('Iteration:', iteration)
		print('PageRank:', page_rank)
		print('Error:', error)

		page_rank = new_page_rank
		iteration += 1

		if error < epsilon:
			break

	print('\nFinal PageRank:', page_rank)
	print('Total iterations:', iteration)


def main():
	graph = {
		's1': ['s2', 's3', 's4', 's5'], 
		's2': ['s1', 's3', 's4', 's5'], 
		's3': ['s1', 's2', 's4'], 
		's4': ['s1', 's2', 's3', 's6'],
		's5': ['s1', 's2', 's6'],
		's6': ['s4', 's5'],
	}

	caculator(graph)
	print('test main')


if __name__ == '__main__':
	main()
