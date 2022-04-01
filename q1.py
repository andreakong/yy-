# Name: Lim Yong Yin    
# Email ID: yongyin.lim.2018

def get_people_with_high_temperatures(ppl_list):
    # Modify the code below.
    result_list = []
    if len(ppl_list) == 0:
        return result_list
    else:
        count = 0
        total_temp = 0
        for tup in ppl_list:
            name = tup [0]
            temp = tup [1:len(tup)]
            for item in temp:
                count += 1
                total_temp += float(item)
                avg_temp = total_temp/count
                if avg_temp > 37.5:
                    if name in result_list:
                        pass
                    else:
                        result_list.append(name)
        return result_list

