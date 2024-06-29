MAX=100
lcslen = 0
dp=[[-1 for i in range(MAX)] for i in range(MAX)]

def lcs(str1, str2, len1, len2, i, j):
	if (i == len1 or j == len2):
		dp[i][j] = 0
		return dp[i][j]
	if (dp[i][j] != -1):
		return dp[i][j]
	ret = 0
	if (str1[i] == str2[j]):
		ret = 1 + lcs(str1, str2, len1, len2, i + 1, j + 1)
	else:
		ret = max(lcs(str1, str2, len1, len2, i + 1, j),
				lcs(str1, str2, len1, len2, i, j + 1))
	dp[i][j] = ret
	return ret

def printAll(str1, str2, len1, len2, data, indx1, indx2, currlcs):
	if (currlcs == lcslen):
		print("".join(data[:currlcs]))
		return
	if (indx1 == len1 or indx2 == len2):
		return
	for ch in range(ord('a'),ord('z') + 1):
		done = False
		for i in range(indx1,len1):
			if (chr(ch)==str1[i]):
				for j in range(indx2, len2):
					if (chr(ch) == str2[j] and dp[i][j] == lcslen-currlcs):
						data[currlcs] = chr(ch)
						printAll(str1, str2, len1, len2, data, i + 1, j + 1, currlcs + 1)
						done = True
						break
				if (done):
					break

def prinlAllLCSSorted(str1, str2):
	global lcslen
	len1,len2 = len(str1),len(str2)
	lcslen = lcs(str1, str2, len1, len2, 0, 0)
	data = ['a' for i in range(MAX)]
	printAll(str1, str2, len1, len2, data, 0, 0, 0)

if __name__ == '__main__':
	str1 = input()
	str2 = input()
	print("Here it goes likes this")
	prinlAllLCSSorted(str1, str2)
