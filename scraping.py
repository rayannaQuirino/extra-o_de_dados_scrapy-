import scrapy 


class main(scrapy.Spider):
    name = 'main'
    start_urls = ['https://repositorio.unesp.br/discover?filtertype=type&filter_relational_operator=equals&filter=Tese+de+doutorado']
    
    def parse(self,response):
        link = response.xpath('//div[@class="col-sm-9 artifact-description"]/a/@href').extract()
        
        for l in link:
            url = f'https://repositorio.unesp.br{l}'
            yield scrapy.Request(url=url,callback=self.parse_article)
            
        next_pag = response.xpath('//a[@class="next-page-link"]/@href').get()
        if next_pag is not None:
            yield scrapy.Request(response.urljoin(next_pag), callback=self.parse)
    
    
    def parse_article(self, response):
        title =response.xpath('//h2[@class="page-header first-page-header"]/text()').extract()
        authors = response.xpath('//div[@class="ds-dc_contributor_author-authority"]/a/text()').extract()
        advisor = response.xpath('//div[@class="ds-dc_contributor_author-authority"]/a/text()').extract()
        date = response.xpath('//div[@class="simple-item-view-date word-break item-page-field-wrapper table"]/text()').extract()
        words= response.xpath('//div[@class="simple-item-view-description item-page-field-wrapper table"]/div/a/text()').extract()
        resume =response.xpath('//p[@class="abstract"]/text()').extract()
        yield{
            'nome': title,
            'autor':authors,
            'orientador':advisor,
            'data de publicação':date,
            'palavras-chave':words, 
            'resumo': resume
        }

        





    
    


        

        
        

        
      




             
            
     
        

        

     
        
        

            