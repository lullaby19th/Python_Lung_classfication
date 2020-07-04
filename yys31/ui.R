shinyUI(
  fluidPage(
    includeCSS("bootstrap.css"),
    
    pageWithSidebar(
      headerPanel(title = 'Lungs classificaiton using DenseNet',
                  windowTitle = 'Lungs classificaiton using DenseNet'),
      
      fluidRow(
        column(1),
        column(9,
               tabsetPanel(
                 id = "tabs",
                 tabPanel("Upload Image",
                          fileInput('file1', 'Upload a PNG / JPEG File:')),
                 tabPanel(
                   "Use the URL",
                   textInput("url", "Image URL:", "http://"),
                   actionButton("goButton", "Go!")
                 )
               ),
               h3(titlePanel("DESCRIPTION - Image Classification")),
               h3(titlePanel("Image Classification"))
               
        ),
        column(2)
      ),
      
      
      mainPanel(
        h3("Image"),
        tags$hr(),
        imageOutput("originImage", height = "auto"),
        tags$hr(),
        h3("What is this?"),
        tags$hr(),
        verbatimTextOutput("res")
      )
      
      
    )))