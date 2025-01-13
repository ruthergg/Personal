
library(tidyverse)
library(readxl)
df=read_excel("sportsdata.xlsx")
colnames(df) <- c('NUM','Year','NumTeams','FGA0-19','FGM0-19','FGA20-29','FGM20-29','FGA30-39',
                  'FGM30-39','FGA40-49','FGM40-49','FGA50+','FGM50+','TFGA','TFGM','FGP','XPA','XPM','XPP')
df <- mutate(df, `FGP0-19` = `FGM0-19`/`FGA0-19`, `FGP20-29` = `FGM20-29`/`FGA20-29`, 
             `FGP30-39` = `FGM30-39`/`FGA30-39`, `FGP40-49` = `FGM40-49`/`FGA40-49`, `FGP50+` = `FGM50+`/`FGA50+`)
library(shiny)
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      selectInput("x", "Kick Statistic", 
                  c("Field Goal %" = "FGP", "Extra Point %" = "XPP",
                    "FG% Between 0-19 Yards" = "`FGP0-19`", "FG% Between 20-29 Yards" = "`FGP20-29`", 
                    "FG% Between 30-39 Yards" = "`FGP30-39`", "FG% Between 40-49" = "`FGP40-49`", 
                    "FG% 50+ Yards" = "`FGP50+`")),
      sliderInput("y", "Year Range", min = 1980, max = 2024, value = c(1980, 2024)),
    ),
    mainPanel(plotOutput(outputId = "Plot"))
  )
)
server <- function(input, output, session) {
  
  output$Plot <- renderPlot({
    df2 <- df[df$Year>=input$y[1]&df$Year<=input$y[2],]
    ggplot(data = df2, aes_string(x = df2$Year, y = input$x)) + geom_smooth(se = FALSE) +scale_y_continuous(labels = scales::percent)
    + theme_classic() + labs(x = "Year", y = "Field Goal Convertion Rate Per Year",title ="Analysis of NFL Kicking",
                             subtitle = "Over the Last 44 Years",
                             caption = "Data: Provided by Pro-Football-Reference.com,
                                Chart By Gabriel Rutherford 
                                            November 13th, 2024")
  })
}
shinyApp(ui = ui, server = server)
