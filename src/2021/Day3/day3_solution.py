import pandas as pd



if __name__ == "__main__":
    with open("day3_input.txt", "r") as f:
        input = f.read()
        input = input.split("\n")

    input_dict = {}

    for i in range(0, len(input[0])):
        input_dict[i] = [k[i] for k in input]

    input_df = pd.DataFrame(input_dict)

    most_common = ''
    least_common = ''

    for col in list(input_df.columns):
        counts = input_df[col].value_counts()
        most_common += list(counts.head(1).index)[0]
        least_common += list(counts.tail(1).index)[0]

    gamma = int(most_common, 2)
    epsilon = int(least_common, 2)

    print(f"PRODUCT: {gamma * epsilon}")


    ### PART 2 ###
    # Oxygen
    filtered_df = input_df
    for col in list(input_df.columns):
        counts = filtered_df[col].value_counts()
        most_common = list(counts.head(1).index)[0]
        least_common = list(counts.tail(1).index)[0]
        if counts.iloc[0] == counts.iloc[1]:
            most_common = '1'

        # if filtered_df.shape[0] == 1:
        #     break

        filtered_df = filtered_df[filtered_df[col] == most_common]
        if filtered_df.shape[0] == 1:
            break


    oxygen_binary = ''
    for col in list(filtered_df.columns):
        oxygen_binary += filtered_df.iloc[0, col]


    # Co2
    filtered_df = input_df
    for col in list(input_df.columns):
        counts = filtered_df[col].value_counts()
        most_common = list(counts.head(1).index)[0]
        least_common = list(counts.tail(1).index)[0]
        if counts.iloc[0] == counts.iloc[1]:
            least_common = '0'



        filtered_df = filtered_df[filtered_df[col] == least_common]
        if filtered_df.shape[0] == 1:
            break

    co2_binary = ''
    for col in list(filtered_df.columns):
        co2_binary += filtered_df.iloc[0, col]

    oxygen_int = int(oxygen_binary, 2)
    co2_int = int(co2_binary, 2)

    print(f"PART 2 PRODUCT: {oxygen_int * co2_int}")

    print("Debug")

