import random
import math

def calcEntropy(sequence):
    modified_numbers = [-e * math.log2(e) for e in sequence]
    return sum(modified_numbers)

def calcNB(sequence, bit):
    return len(sequence.keys()) * (bit + 8)

def calculate_average(array):
    total = sum(array)
    average = total / len(array)
    return average

def findPhrases(input_str, keys_dict):
    ind = 0
    inc = 1
    i = 1
    while True:
        if not (len(input_str) >= ind+inc):
            break
        sub_str = input_str[ind:ind + inc]
        if sub_str in keys_dict:
            inc += 1
        else:
            keys_dict[sub_str] = i
            i += 1
            ind += inc
            inc = 1

def find_phrases(num_of_bits, keys_dict):
    temp = {}
    for present_value in keys_dict.keys():
        if len(present_value) == 1:
            temp[present_value] = '0'.rjust(num_of_bits, '0') + present_value[0]
        else:
            for past_value, past_key in keys_dict.items():
                if present_value[:len(present_value) - 1] == past_value:
                    temp[present_value] = str(bin(past_key).replace("0b","")).rjust(num_of_bits, '0')\
                                          + present_value[len(present_value) - 1]
    return temp

def LZW(probabilities):
    for N in (20, 50, 100, 200, 400, 800, 1000, 2000):
        compressionValues = []
        NB_Values = []
        numOfBitsPerSymbol = []
        for i in range(0, 5):
            random_sequence = random.choices(list(probabilities.keys()),
                                             list(probabilities.values()), k=N)
            input_str = "".join(random_sequence)
            keys_dict = {}
            findPhrases(input_str, keys_dict)
            bits = math.ceil(math.log2(len(keys_dict.items())))
            codewords = find_phrases(bits, keys_dict)
            NB = calcNB(keys_dict, bits)
            BPS = NB / N
            NB_Values.append(NB)
            compressionValues.append(NB / (N * 8))
            numOfBitsPerSymbol.append(BPS)
        print(f"{str(N):>12}" + "\t\t" +
              str(calculate_average(NB_Values)) + "\t\t" +
              str(round(calculate_average(compressionValues) * 100, 2)) +"%"
              + "\t\t" + str(round(calculate_average(numOfBitsPerSymbol),
                                   2)) + "\t\t")

def main():
    probabilities = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}
    print("Entropy H = " + str(calcEntropy(probabilities.values())) +
          "bits\n")
    print("********************************************************")
    print("\t\t N\t\t\tNB\t\t\tNB/8*N\t\tNB/N")
    LZW(probabilities)
    if __name__ == "__main__":
        main()

