#1.
sikasso_data =  pd.read_csv('data/sikasso_aq.csv')


#2.
#a.

sikasso_data['Date'] = pd.to_datetime(sikasso_data['Date'] )
sikasso_data['dates'] =  sikasso_data['Date'].dt.date
sikasso_data["year"] = sikasso_data["Date"].dt.year

sikasso_data["month"] = sikasso_data["Date"].dt.month

sikasso_data["day"] = sikasso_data["Date"].dt.day

sikasso_data['time'] =  sikasso_data['Date'].dt.time
sikasso_data.head()


#b.
pm10_data = pd.DataFrame(sikasso_data.groupby('month')['Con_PM10'].mean()).reset_index()
pm10_data['month_name'] = pd.to_datetime(pm10_data['month'], format='%m').dt.month_name().str.slice()


#c.
plt.figure(figsize=(14,4))
plt.plot(pm10_data['month_name'] , pm10_data['Con_PM10'])
plt.xlabel('month')
plt.ylabel('Con_PM10 avg')
plt.title('Evolution of Con_PM10 average')

#3.
#month with the lowest
pm10_data.iloc[pm10_data['Con_PM10'].idxmin(),:]

#month with the largest
pm10_data.iloc[pm10_data['Con_PM10'].idxmax(),:]


#4.

def monthly_insights(data_frame,  polluant ):
    grouped = pd.DataFrame(data_frame.groupby('month')[polluant].mean()).reset_index()
    grouped['month_name']= pd.to_datetime(grouped['month'], format='%m').dt.month_name().str.slice()
    return grouped

def plot_polluants_avgs(data_frame,  polluant ):
    import random
    colors =  ['r' , 'b' , 'g' , 'k', 'cyan' ,'magenta']
    plt.figure(figsize=(18,6))
    plt.plot(data_frame['month_name'] , data_frame[polluant] , color =  random.choice(colors))
    plt.xlabel('month')
    plt.ylabel('Average of ' + polluant)
    plt.title('Evolution of '+ polluant + ' Averages ')
    plt.show()
    return 
    
    
    
polluants_list = sikasso_data.columns[1:7]

for pol in polluants_list:
    
    pol_x =  monthly_insights(sikasso_data , pol)
    print("for ", pol ," the lowest average is ",pol_x.iloc[pol_x[pol].idxmin(),1] , " which corresponds to ",pol_x.iloc[pol_x[pol].idxmin(),-1] )
    print(" and the largest average is ",pol_x.iloc[pol_x[pol].idxmax(),1] , " which corresponds to ",pol_x.iloc[pol_x[pol].idxmax(),-1] )
    print("\n")
    
    
polluants_list = sikasso_data.columns[1:7]

for pol in polluants_list:
    pol_x =  monthly_insights(sikasso_data , pol)
    plot_polluants_avgs(pol_x , pol)
    
    
 
#5.
sikasso_data.set_index('Date', inplace=True)
quaterlies_data = sikasso_data.groupby(pd.Grouper(freq='4M'))
monthAvg_pols = quaterlies_data[polluants_list].mean().reset_index()
monthAvg_pols

