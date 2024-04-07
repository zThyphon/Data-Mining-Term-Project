import matplotlib.pyplot as plt

#Bar Chart Draw Function
def draw_bar_chart(xAxisValues,yAxisValues,xLabel,yLabel,chart_title):
    #Create Bars According to Inputs
    plt.bar(xAxisValues,yAxisValues)

    #Specify X Axis Label
    plt.xlabel(xLabel)

    #Specify Y Axis Label
    plt.ylabel(yLabel)

    #Specify Bar Chart Title
    plt.title(chart_title)

    #Show the Chart
    plt.show()

#Pie Chart Chart Draw Function
def draw_pie_chart(labels,percentages,chart_title):
    #Specify Pie Colors
    colors = ["gold", "orange", "yellow","lightcoral", "lightskyblue", "green", "pink"]

    #Plot the Pie Chart 
    plt.figure(figsize=(10, 10))

    #Specify Pie Settings
    plt.pie(percentages, labels=labels, colors=colors, autopct='%1.1f%%', 
            shadow=True, startangle=140)
    plt.axis("equal")  

    plt.title(chart_title)

    #Display the Chart
    plt.show()