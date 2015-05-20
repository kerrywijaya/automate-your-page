#the output of this program is an HTML string that can be copied and pasted into the HTML editor
#unfortunately, the identation won't come out correctly after being pasted into HTML file :(
#one or more concepts can be added to a list of concepts (my_concepts)
#refinements have to be made within the HTML file

def generate_HTML(h1id, heading, subtitle, description): 
#generates HTML out of each concept                
   part1 = '''

      <h1 id="''' + h1id
   part2 = '''">
         ''' + heading + ''' '''+'''
      <span class="subtitle">''' + subtitle
   part3 = '''</span>
      </h1>

      <div class="content">
         ''' + description
   part4 = '''
      </div>'''
   concept = part1 + part2 + part3 + part4
   return concept

def my_HTML(any_list):
#would work for any list but is especially supposed to make an HTML string out of my_concepts
    HTML = ''
    for e in any_list:
        this_id = e[0]
        this_head = e[1]
        this_sub = e[2]
        this_des = e[3]          
        HTML += generate_HTML(this_id, this_head, this_sub, this_des)
    return HTML

#my_concepts is a list that is filled with new concepts while running the program
#each concept is itself a list consisting of id, heading, subtitle and description 
my_concepts = []

def add_concept(new_id, new_heading, new_subtitle, new_description):
#adds new concept to my_concepts
   new_concept = [new_id, new_heading, new_subtitle, new_description]
   my_concepts.append(new_concept)
   return my_concepts


#call add_concept() to add a new concept
#print my_concepts to see what's in my_concepts
#print my_HTML(my_concepts) to get the whole HTML of all concepts in the list





  












