import plotly.express as px
import us

def choropleth(final_data_set):
    df = final_data_set

    df["States"] = df["States"].str.strip()

    def get_abbr(name):
        if name == "District of Columbia":
            return "DC"
        state = us.states.lookup(name)
        return state.abbr
    
    df["States"] = df["States"].apply(get_abbr)

    color_scale = ["green", "yellow", "orange", "red"]

    fig = px.choropleth(
        df,
        locations="States",
        locationmode="USA-states",
        color="Avg_PM25",
        scope="usa",
        color_continuous_scale=color_scale,
        range_color=(df["Avg_PM25"].min(), df["Avg_PM25"].max()),
        labels={"Avg_PM25": "Average PM2.5"},
    )

    fig.show()

def high_and_low(final_data_set):
 
    df = final_data_set
    
    
    columns_to_summarize = [
        "Not_graduated", "HDI", "Health_Index",
        "Education_Index", "Income_Index",
        "Homeless_Ratio", "Unsheltered_Homeless", "Avg_PM25"
	]
    
    summary = []
    
    for col in columns_to_summarize:
        mean_val = df[col].mean()
        std_val = df[col].std()
        max_val = df[col].max()
        min_val = df[col].min()
        state_max = df.loc[df[col].idxmax(), "States"]
        state_min = df.loc[df[col].idxmin(), "States"]
        
        summary.append({
		    "Variable": col,
		    "Average ± SD": f"{mean_val:.2f} ± {std_val:.2f}",
		    "Highest State": f"{state_max} ({max_val:.2f})",
		    "Lowest State": f"{state_min} ({min_val:.2f})"
		})
    summary_df = pd.DataFrame(summary)
    print(summary_df)    