\[
Error = \max_i |PR_{t+1}(S_i)-PR_t(S_i)|
\]

\[
\boxed{Error < \epsilon}
\]

\[
\epsilon = 0.000001 = 10^{-6}
\]


graph = {
    's1': ['s2', 's3', 's4', 's5'], 
    's2': ['s1', 's3', 's4', 's5'], 
    's3': ['s1', 's2', 's4'], 
    's4': ['s1', 's2', 's3', 's6'],
    's5': ['s1', 's2', 's6'],
    's6': ['s4', 's5'],
}

damping 
# damping factor (Google đề xuất và sử dụng phổ biến để mô phỏng hành vi người dùng khi duyệt web)
	# 85% khả năng: Người dùng tiếp tục nhấn vào một liên kết trên trang hiện tại để chuyển sang trang khác.
	# 15% khả năng: Người dùng không nhấn liên kết hiện tại mà chuyển ngẫu nhiên sang một trang khác.