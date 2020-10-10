class Segment:
    left = 0
    right = 0

class SegmentDecode(Segment):
    character = None

def define_segments(letters, probability):
    l = 0
    segments = {letter: Segment() for letter in letters}
    print (letters)

    for i in range(len(letters)):
        segments[letters[i]].left = l
        segments[letters[i]].right = l + probability[i]
        l = segments[letters[i]].right
        print (letters[i], segments[letters[i]].left, segments[letters[i]].right)
    
    return segments


def arithmetic_encoding(letters, probability, s):
        segments = define_segments(letters, probability)
        left = float(0)
        right = float(1)

        for i in range(len(s)):
            symb = s[i]
            new_right = left + (right - left) * segments[symb].right
            new_left = left + (right - left) * segments[symb].left
            left = new_left
            right = new_right

        return (left + right) / 2


def define_segments_decode(letters, probability):
    l = 0
    segments = [SegmentDecode() for i in range(len(letters))]

    for i in range(len(letters)):
        segments[i].left = l
        segments[i].right = l + probability[i]
        segments[i].character = letters[i]
        l = segments[i].right

    return segments


def arithmetic_decoding(letters, probability, code, n):
    segments = define_segments_decode(letters, probability)
    s = ""

    for i in range(n):
        for j in range(len(letters)):
            if segments[j].left <= code < segments[j].right:
                s += segments[j].character
                code = (code - segments[j].left) / (segments[j].right - segments[j].left)
                break
    return s



def main():
    string = "AADABDCCCC"
    probability = [string.count(i) / len(string) for i in sorted(set(list(string)))]

    print(probability)

    encoded = arithmetic_encoding(letters=sorted(list(set(list(string)))), probability=probability, s=string)
    print(encoded)

    decoded = arithmetic_decoding(letters=sorted(list(set(list(string)))), probability=probability, code=encoded, n=len(string))
    print(decoded)

    decoded2=arithmetic_decoding(letters=sorted(list(set(list(string)))), probability=probability, code=0.92064,n=5)

    print(decoded2)
main()