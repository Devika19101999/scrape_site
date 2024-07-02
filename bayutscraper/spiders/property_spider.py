import scrapy


class BayutSpider(scrapy.Spider):
    name = 'bayut'
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    def parse(self, response):
        for property in response.css('div._31a7ce0c f55e23e5'):

         try:

            yield {
                "property_id":property.css("ul._3dc8d08d li:nth-child(3) span._2fdf7fc5::text").get(),
                 "purpose":property.css("ul._3dc8d08d li:nth-child(2) span._2fdf7fc5::text").get(),
                 "type":property.css("ul._3dc8d08d li:nth-child(1) span._2fdf7fc5::text").get(),
                 "added_on": property.css("ul._3dc8d08d li:last-child span._2fdf7fc5::text").get(),
                 "furnishing":property.css("ul._3dc8d08d li:nth-child(4) span._2fdf7fc5::text").get(),

                 "price": {
                               "currency": property.css("div._2923a568 span::text").get(),
                                "amount":  property.css("div._2923a568 span[aria-label='Price']::text").get()
                            },
                 "location":  property.css("div.e4fd45f0::text").get(),
                
              "bed_bath_size":{
                                  "bedrooms":property.css("div._14f36d85 span[aria-label='Beds'] span._140e6903::text").get(),
                                  "bathrooms":property.css("div._14f36d85 span[aria-label='Baths'] span._140e6903::text").get(),
                                  "size": property.css("div._10fef2e8 span[aria-label='Area'] span span::text").get()
                                  
                                },

                 
                  "agent_name": property.css("div._948d9e0a._2f598d31._95d4067f span._4c376836 a::text").get(),
              
                "image_url":property.css('source::attr(srcset)').get(),

                "breadcrumbs": property.css("div._3624d529 a span::text").getall(),
              "amenities" : [
                  property.css("div.da8f482a div._117b341a div._682538c2 div._01ade828 span::text").getall()
                  ],
              "description ": property.css("div._1e8e64c5 span::text").getall() 
              
              }
            
         except:
            
            yield {
                "property_id":property.css("ul._3dc8d08d li:nth-child(3) span._2fdf7fc5::text").get(),
                 "purpose":property.css("ul._3dc8d08d li:nth-child(2) span._2fdf7fc5::text").get(),
                 "type":property.css("ul._3dc8d08d li:nth-child(1) span._2fdf7fc5::text").get(),
                 "added_on": property.css("ul._3dc8d08d li:last-child span._2fdf7fc5::text").get(),
                 "furnishing":property.css("ul._3dc8d08d li:nth-child(4) span._2fdf7fc5::text").get(),

                 "price": "sold out",

                 "location":  property.css("div.e4fd45f0::text").get(),
                
              "bed_bath_size":{
                                  "bedrooms":property.css("div._14f36d85 span[aria-label='Beds'] span._140e6903::text").get(),
                                  "bathrooms":property.css("div._14f36d85 span[aria-label='Baths'] span._140e6903::text").get(),
                                  "size": property.css("div._10fef2e8 span[aria-label='Area'] span span::text").get()
                                  
                                },

                
                  "agent_name": property.css("div._948d9e0a._2f598d31._95d4067f span._4c376836 a::text").get(),
              
                "image_url":property.css('source::attr(srcset)').get(),

                "breadcrumbs": property.css("div._3624d529 a span::text").getall(),

              "amenities" : [
                  property.css("div.da8f482a div._117b341a div._682538c2 div._01ade828 span::text").getall()
                  ],
              "description ": property.css("div._1e8e64c5 span::text").getall() 
              
              }

            
        next_page= "https://www.bayut.com" + response.css("a[href*='page-2']::attr(href)").get()
        if next_page:
           next_page = "https://www.bayut.com" + next_page
           yield response.follow(next_page, self.parse)
    
    
    
        
            
         