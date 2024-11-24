# prompt: I have three folders in one main folder and each folder i have one josn file now i need to plot graph of each json file and save with same folder name  how to do it i have code for plotting graph

import json
import matplotlib.pyplot as plt
import numpy as np
import os

# Path to the main folder containing subfolders with JSON files
main_folder_path = '/home/prasanjith/Desktop/Atr/Atr/TrainTest/shortSet1'  # Replace with the actual path
# Iterate through the subfolders in the main folder
for folder_name in os.listdir(main_folder_path):
    folder_path = os.path.join(main_folder_path, folder_name)

    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Iterate through the time-based subfolders
        for timeline_folder in os.listdir(folder_path):
            timeline_folder_path = os.path.join(folder_path, timeline_folder)

            # Check if it's a directory and find the JSON file
            if os.path.isdir(timeline_folder_path):
                for filename in os.listdir(timeline_folder_path):
                    if filename.endswith(".json"):
                        json_filepath = os.path.join(timeline_folder_path, filename)

                        try:
                            with open(json_filepath, 'r') as f:
                                data = json.load(f)

                            test_result_net_profit = []
                            train_result_net_profit = []

                            for i in range(len(data)):
                                test_result_net_profit.append(data[i]['testResult']['netProfit'])
                                train_result_net_profit.append(data[i]['trainResult']['netProfit'])

                            train_result_net_profit = [-i for i in train_result_net_profit]
                            train_result_net_profit_negative = train_result_net_profit
                            x_positions = np.arange(len(train_result_net_profit))

                            plt.figure(figsize=(10, 6))
                            plt.bar(x_positions, test_result_net_profit, color='green', label='Test Net Profit')
                            plt.bar(x_positions, train_result_net_profit_negative, color='blue', label='Train Net Profit')
                            plt.axhline(0, color='black', linestyle='--', label='Baseline (0)')
                            plt.xticks(x_positions, [f'DP {i+1}' for i in x_positions])
                            plt.text(0.98, -0.15, 'Net Profit: Test Above, Train Below', fontsize=10, ha='right', transform=plt.gcf().transFigure)
                            plt.legend(loc='lower right', bbox_to_anchor=(0.98, 0.02))

                            # Save the plot with the same folder name
                            plt.savefig(os.path.join(timeline_folder_path, f'{timeline_folder}_plot.png'))
                            plt.close()  # Close the plot to free up memory
                            print(f"Plot saved for {timeline_folder}")

                        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
                            print(f"Error processing {json_filepath}: {e}")