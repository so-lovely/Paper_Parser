# %%
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

from pathlib import Path

# %%
"""
-linkbot arguments-
past_data = {page1_url: {element1 : {tag:[tag1, tag2, tag3, tag4 ....], -> history
                                     text: [.....]
                                     value:
                                     ...
                                     function: hash(function)
                                     }
                     element2 : {tag:[(another)tag1, tag2, tag3, tag4 ....],
                                 text: [....]
                                 value:
                                 function: '  '
                                 ...
                                 }
                                 }
                     ....
                     }
        page2_url: ....
        }

current_data = { element1:{id : 
                           tag:
                           text:
                           value:
                          function:    hash(function)
                          }
                 element2: {
                 ...
                                }
                .....
                }
current_element = {id:
                   tag:
                   text:
                   link_text:
                   function: hash(function)
                   ..
                   }


current element is required
Going to next page, current_element should be cleared

"""

# %%
"""
Default find function param -> one_param = False, filter = True, reset = False
"""

"""
OPEN:
If reset with find function, what about history?
"""

"""
Working on linkbot.py not linkbot_test.ipynb May 16 around 12 p.m
"""

# %%
class Linkbot:
    def __init__(self, url):
        self.starturl = url
        self.past_data = {}
        self.current_data = {}
        self.current_element_info = {}
        self.current_element = None
        self.current_elements = None
        self.driver = None
        self.current_url = None
        self.is_update_current_element = None
        self.fun_name = None
        self.pass_current_element = None
        self.one_param = None


    def startpoint_load(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.starturl)
        self.driver.implicitly_wait(2)
        self.current_url = self.driver.current_url
        

    def find_elements_by_tag(self, tag:str, filter=True, one_param=False):
        temp_fun_name:str = 'find_elements_by_tag_a'
        self.current_url = self.driver.current_url
        if one_param == False:
            if filter == True:
                filter_elements = []
                for element in self.current_elements:
                    self.current_element = element.find_element(by=By.TAG_NAME, value=tag)
                    filter_elements.append(self.current_element)
                    self.processing_elements(fun_name=temp_fun_name, value=tag, one_param=True, tag=tag)
                self.current_elements = filter_elements
                return filter_elements
            elif filter == False:
                self.current_elements = self.driver.find_elements(by=By.TAG_NAME, value=tag)
                self.processing_elements(fun_name=temp_fun_name, value=tag, tag=tag)
                return self.current_elements
            else:
                raise RuntimeError(" ".join([temp_fun_name ,'error - filter is not bool']))
        elif one_param == True:
            if filter == True:
                self.current_element = self.current_element.find_element(by=By.TAG_NAME, value=tag)
                self.processing_elements(fun_name=temp_fun_name, value=tag, one_param=True, tag=tag)
                return self.current_element
            else:
                self.current_element = self.driver.find_element(by=By.TAG_NAME, value=tag)
                self.processing_elements(fun_name=temp_fun_name, value=tag, one_param=True, tag=tag)
                return self.current_element
        else:
            assert False, print('One_param is not bool')        
    def filter_hrefs(self, index:int, string): # -> elements
        filtered_elements = []
        self.current_url = self.driver.current_url
        for element in self.current_elements:
            if len(Path(element.get_attribute('href')).parts) < index + 1:
                pass
            elif string in Path(element.get_attribute('href')).parts[index]:
                self.current_element = element
                filtered_elements.append(self.current_element)
                self.processing_elements(fun_name='filter_hrefs', value=string, one_param=True)
            else:
                pass
        self.current_elements = filtered_elements
        return filtered_elements


    def get_ids(self, elements=None, one_param = False): 
        if elements is None:
            if one_param == True:
                return self.current_element.get_attribute('id')
            elif one_param == False:
                elements_ids = []
                for element in self.current_elements:
                    elements_ids.append(element.get_attribute('id'))
                return elements_ids
            else:
                assert False, 'Check get_ids - elements is None & one_param is not bool'
        else:
            if one_param == True:
                return elements.get_attribute('id')
            elif one_param == False:
                elements_ids = []
                for element in elements:
                    elements_ids.append(element.get_attribute('id'))
                return elements_ids
            else:
                assert False, 'Check get_ids = elements is not None & one_param is not bool'
            
                

    def find_elements_by_id(self,id, filter=True, one_param=False):
        temp_fun_name:str = 'find_elements_by_id'
        self.current_url = self.driver.current_url
        if one_param == False:
            if filter == True:
                filter_elements = []
                for element in self.current_elements:
                    self.current_element = element.find_element(by=By.ID, value=id)
                    filter_elements.append(self.current_element)
                    self.processing_elements(fun_name=temp_fun_name, value=id, one_param=True)
                self.current_elements = filter_elements
                return filter_elements
            elif filter == False:
                self.current_elements = self.driver.find_elements(by=By.ID, value=id)
                self.processing_elements(fun_name=temp_fun_name, value=id)
                return self.current_elements
            else:
                raise RuntimeError(" ".join([temp_fun_name ,'error - filter is not bool']))
        elif one_param == True:
            if filter == True:
                self.current_element = self.current_element.find_element(by=By.ID, value=id)
                self.processing_elements(fun_name=temp_fun_name, value=id, one_param=True)
                return self.current_element
            else:
                self.current_element = self.driver.find_element(by=By.ID, value=id)
                self.processing_elements(fun_name=temp_fun_name, value=id, one_param=True)
                return self.current_element
        else:
            assert False, print('One_param is not bool')
    
    
    def click_element(self): 
        self.driver.click()
        time.sleep(1)
        self.current_url = self.driver.current_url
        self.current_element_and_elements_clear()
        

    def find_elements_by_link_text(self, link_text:str, filter=True, one_param = False): 
        temp_fun_name:str = 'find_elements_by_link_text'
        self.current_url = self.driver.current_url
        if one_param == False:
            if filter == True:
                filter_elements = []
                for element in self.current_elements:
                    self.current_element = element.find_element(by=By.LINK_TEXT, value=link_text)
                    filter_elements.append(self.current_element)
                    self.processing_elements(fun_name=temp_fun_name, value=link_text, one_param=True)
                self.current_elements = filter_elements
                return filter_elements
            elif filter == False:
                self.current_elements = self.driver.find_elements(by=By.LINK_TEXT, value=link_text)
                self.processing_elements(fun_name=temp_fun_name, value=link_text)
                return self.current_elements
            else:
                raise RuntimeError(" ".join([temp_fun_name ,'error - filter is not bool']))
        elif one_param == True:
            if filter == True:
                self.current_element = self.current_element.find_element(by=By.LINK_TEXT, value=link_text)
                self.processing_elements(fun_name=temp_fun_name, value=link_text, one_param=True)
                return self.current_element
            else:
                self.current_element = self.driver.find_element(by=By.LINK_TEXT, value=link_text)
                self.processing_elements(fun_name=temp_fun_name, value=link_text, one_param=True)
                return self.current_element
        else:
            assert False, print('One_param is not bool')

    def current_element_and_elements_clear(self): 
        self.current_element.clear()
        self.current_elements.clear()


    def forward(self):
        self.driver.forward()
        time.sleep(1)
        self.current_url = self.driver.current_url
        self.current_element_and_elements_clear()
    

    def back(self):
        self.driver.back()
        time.sleep(1)
        self.current_url = self.driver.current_url
        self.current_element_and_elements_clear()
        

    def quit(self):
        time.sleep(1)
        self.driver.quite()

        #The function below updates current_element_info & current_data_info % past_data_info
    def update_current_element_info(self, function=None, Value=None, tag=None):
        tag_name, value_name, function_name = [],[],[]
        if len(self.past_data) == 0:
            tag_name.append(tag)
            value_name.append(None if Value is None else Value)
            function_name.append(None if function is None else hash(function))
        elif self.current_element in self.past_data[self.current_url].keys():
            past_data_tag:list = self.past_data[self.current_url][self.current_element]['tag']
            past_data_value:list = self.past_data[self.current_url][self.current_element]['value']
            past_data_function:list = self.past_data[self.current_url][self.current_element]['function']
            tag_name:list = past_data_tag.append(tag)
            value_name:list = past_data_value.append(None if Value is None else Value)
            function_name:list = past_data_function.append(None if function is None else hash(function))
        elif self.current_element:
            tag_name.append(tag)
            value_name.append(None if Value is None else Value)
            function_name.append(None if function is None else hash(function))
        else:
            raise RuntimeError('if-else condition error at update_current_element_info')
        self.pass_current_element = {'id': self.current_element.get_attribute('id'),
                          'tag': tag_name, 
                          'text': self.current_element.text,
                          'value': value_name, 
                          'function': function_name} 
        self.current_element_info.update(self.pass_current_element)
        self.is_update_current_element = True
        self.update_current_data_info(self.pass_current_element) 
        self.update_past_data_info(self.pass_current_element)
        self.is_update_current_element = False


    def update_current_data_info(self, pass_element):
        if self.is_update_current_element == True:
            self.current_data.update({self.current_element : pass_element})
        else:
            raise RuntimeError('update_current_data_info error')


    def update_past_data_info(self, pass_element):
        if self.is_update_current_element == True:
            if not self.current_url in self.past_data.keys():
                self.past_data.update({self.current_url:{self.current_element : pass_element}})
            else:
                self.past_data[self.current_url].update({self.current_element : pass_element})
        else:
            raise RuntimeError('update_past_date_info error')
        
        #processing_elements function unifies all updating functions
    def processing_elements(self, fun_name=None, value=None, one_param = False, tag=None):
        if one_param == False:
            for current_element in self.current_elements:
                self.current_element = current_element
                self.update_current_element_info(function=fun_name, Value=value, tag=tag)
        elif one_param == True:
            self.update_current_element_info(function=fun_name, Value=value, tag=tag)
        else:
            raise RuntimeError('processing_elements error')


