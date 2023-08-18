import time

def structure_quad_pairs(coin_list):

    start_time = time.time() 

    quad_pairs_list = []
    remove_duplicates_list = []
    pairs_list = coin_list
    ticker_to_avoid_list = []

    for pair_a in coin_list:

        # Initialize the pair 
        pair_a_split = pair_a.split("/")
        a_base = pair_a_split[0]
        a_quote = pair_a_split[1]
        pair_a_box = [a_base, a_quote]

        tickers_dict = {}
        tickers_dict[f'{a_base}'] = 1
        tickers_dict[f'{a_quote}'] = 1

        print(tickers_dict)

        for pair_b in coin_list:

            if pair_b != pair_a:

                # Initialize the pair 
                pair_b_split = pair_b.split("/")
                b_base = pair_b_split[0]
                b_quote = pair_b_split[1]
                pair_b_box = [b_base, b_quote]

                if b_base in list(tickers_dict.keys()) or b_quote in list(tickers_dict.keys()):
                    
                    # Append the dict
                    if b_base in list(tickers_dict.keys()):
                        tickers_dict[f'{b_base}'] += 1
                        tickers_dict[f'{b_quote}'] = 1


                    if b_quote in list(tickers_dict.keys()):
                        tickers_dict[f'{b_quote}'] += 1
                        tickers_dict[f'{b_base}'] = 1
                    
                    print(tickers_dict)


                for pair_c in coin_list:

                    if pair_c != pair_a and pair_c != pair_b:

                        # Initialize the pair 
                        pair_c_split = pair_c.split("/")
                        c_base = pair_c_split[0]
                        c_quote = pair_c_split[1]
                        pair_c_box = [c_base, c_quote]

                        if (c_base in list(tickers_dict.keys()) or c_quote in list(tickers_dict.keys())) and not (c_base in list(tickers_dict.keys()) and c_quote in list(tickers_dict.keys())):
                            

                            if c_base not in list(tickers_dict.keys()) and tickers_dict[f'{c_quote}'] < 2:
                                tickers_dict[f'{c_base}'] = 1
                                tickers_dict[f'{c_quote}'] += 1

                                print(tickers_dict)

                                tickers_with_count_one = [ticker for ticker, count in tickers_dict.items() if count == 1]
                                print(tickers_with_count_one)


                                for pair_d in coin_list:

                                    if pair_d != pair_a and pair_d != pair_b and pair_d != pair_c:

                                        # Initialize the pair 
                                        pair_d_split = pair_d.split("/")
                                        d_base = pair_d_split[0]
                                        d_quote = pair_d_split[1]
                                        pair_d_box = [d_base, d_quote]


                                        if d_base in tickers_with_count_one and d_quote in tickers_with_count_one:

                                            combined = [pair_a, pair_b, pair_c, pair_d]
                                            unique_item = ''.join(sorted(combined))
                                            if unique_item not in remove_duplicates_list:
                                                print(combined)
                                                remove_duplicates_list.append(unique_item)
                                                quad_pairs_list.append(combined)

                            
                            if c_quote not in list(tickers_dict.keys()) and tickers_dict[f'{c_base}'] < 2:
                                tickers_dict[f'{c_base}'] += 1
                                tickers_dict[f'{c_quote}'] = 1

                                print(tickers_dict)

                                tickers_with_count_one = [ticker for ticker, count in tickers_dict.items() if count == 1]
                                print(tickers_with_count_one)
                        
                                for pair_d in coin_list:

                                    if pair_d != pair_a and pair_d != pair_b and pair_d != pair_c:

                                        # Initialize the pair 
                                        pair_d_split = pair_d.split("/")
                                        d_base = pair_d_split[0]
                                        d_quote = pair_d_split[1]
                                        pair_d_box = [d_base, d_quote]


                                        if d_base in tickers_with_count_one and d_quote in tickers_with_count_one:

                                            combined = [pair_a, pair_b, pair_c, pair_d]
                                            unique_item = ''.join(sorted(combined))
                                            if unique_item not in remove_duplicates_list:
                                                print(combined)
                                                remove_duplicates_list.append(unique_item)
                                                quad_pairs_list.append(combined)

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.4f} seconds")
    return quad_pairs_list

