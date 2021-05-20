
### Sort
电压和电流测量结果的顺序调整。
```python
    # 注意list的sort方法是直接修改对象本身的，所以要先改电压，再改电流
	# 1. old method
    u_data.sort(key=dict(zip(u_data, i_data)).get)

	# 2. new method
    u_data = [el for _, el in sorted(zip(i_data, u_data), key=lambda pair: pair[0])]

	# 3. new method shortest
    u_data = [el for _, el in sorted(zip(i_data, u_data))]


    i_data.sort()
    # 倒序，负电流在前。
    x = i_data = i_data[::-1]
    y = u_data = u_data[::-1]
```

