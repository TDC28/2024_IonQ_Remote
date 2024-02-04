import matplotlib.pyplot as plt


def plot_good(res, n):
    # Convert keys to integers and sort them
    keys_as_int = sorted(map(int, res.keys()))

    # Convert integers to binary representation in big endian
    binary_labels = [format(key, f'0{n}b') for key in keys_as_int]
    print(binary_labels)

    # Extract corresponding values
    values = [res[str(key)] for key in keys_as_int]

    # Plotting
    plt.bar(binary_labels, values)
    plt.xlabel('Binary Number (Big Endian)')
    plt.ylabel('Value')
    plt.title('Histogram of Result Object')
    plt.show()


def probability(res, n):
    keys_as_int = sorted(map(int, res.keys()))
    ans = {}

    # Convert integers to binary representation in big endian
    binary_labels = [format(key, f'0{n}b') for key in keys_as_int]

    for i in range(n):
        for j in range(len(binary_labels)):
            if binary_labels[j][i] == '0':
                if i in ans:
                    ans[i] += res[str(keys_as_int[j])]

                else:
                    ans[i] = res[str(keys_as_int[j])]

    return ans