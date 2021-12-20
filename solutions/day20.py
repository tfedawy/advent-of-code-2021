from collections import defaultdict


class EnhancementAlgo:
    def __init__(self, algorithm):
        self.__algorithm = algorithm

    def get_enhancement(self, binary_number):
        binary_number = list(binary_number)
        for i, v in enumerate(binary_number):
            binary_number[i] = '0' if v == '.' else '1'
        binary_number = ''.join(binary_number)
        number = int(binary_number, 2)
        return self.__algorithm[number]

    def __str__(self):
        return f'{self.__algorithm}'

    def __repr__(self):
        return self.__str__()

    @property
    def algorithm(self):
        return self.__algorithm


class Image:
    def __init__(self, image, algo):
        self.image = image
        self.squares = None
        self.enhancement_algorithm = EnhancementAlgo(algo)

    def pad_image(self, fill='.', n=1):
        for i in range(n):
            self.image = [[fill] * len(self.image[0])] + self.image + [[fill] * len(self.image[0])]
            self.image = [[fill] + row + [fill] for row in self.image]

    def update_squares(self, fill):
        pixels_squares = defaultdict(str)
        for r, row in enumerate(self.image):
            for c, pixel in enumerate(row):
                neighbors = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c),
                             (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
                for neighbor in neighbors:
                    neighbor_row, neighbor_col = neighbor
                    if 0 <= neighbor_row < len(self.image) and 0 <= neighbor_col < len(row):
                        pixels_squares[r, c] += self.image[neighbor_row][neighbor_col]
                    else:
                        pixels_squares[r, c] += fill
        self.squares = pixels_squares

    def enhance(self, fill):
        self.pad_image(fill)
        self.update_squares(fill)
        for r, row in enumerate(self.image):
            for c, pixel in enumerate(row):
                enhancement = self.enhancement_algorithm.get_enhancement(self.squares[r, c])
                self.image[r][c] = enhancement

    def remove_edges(self):
        self.image = [row[1:-1] for row in self.image]
        self.image = self.image[1:-1]

    def lit_pixels_count(self):
        count = 0
        for row in self.image:
            for value in row:
                if value == '#':
                    count += 1
        return count

    def __str__(self):
        img = [''.join(row) for row in self.image]
        img = '\n'.join(img)
        return img

    def __repr__(self):
        return self.__str__()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n\n')
    enhancement_algorithm = input_data[0]
    img = input_data[1]
    img = img.split('\n')
    img = [list(row) for row in img]

    return img, enhancement_algorithm


def enhance_image(image, n):
    for i in range(n):
        if i % 2 == 0:
            fill = '.'
        else:
            fill = image.enhancement_algorithm.algorithm[0]
        image.enhance(fill)
    return image


def part1(image, n):
    image = enhance_image(image, n)
    return image.lit_pixels_count()


def part2(image, n):
    image = enhance_image(image, n)
    return image.lit_pixels_count()


def main():
    day = '20'
    img, enhancement_algorithm = data_prep(day)
    image = Image(img, enhancement_algorithm)

    answer1 = part1(image, 2)
    answer2 = part2(image, 48)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')
    # print(image)


if __name__ == "__main__":
    main()
