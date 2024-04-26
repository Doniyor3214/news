# a=100000
# for i in a:
#     print(i//1000)

# # for i in str/list/range():
# #     pass
    

#         <center>
        
#         <h1>News detail page</h1>
#         <h2>{{ yangilik.title }}
#         </h2>
#         <p>{{yangilik.text}} | {{yangilik.created}} | {{yangilik.views}} | {{yangilik.author.username}}| {{yangilik.tur.name}}</p>
#         <img src="{{ yangilik.rasm.url }}" alt="" style="width: 500px;">
 
#          <h3>{{one.sarlavha}}</h3>
#         <p>{{one.matn}}</p>
    

            
#         <br>
#         <a href="{% url 'ochirish' yangilik.id %}">delete</a>
#         <a href="{% url 'tahrirlash' yangilik.id %}">edit</a>
#         <hr> 
#     <h1 style="color: rgb(20, 20, 164);">Comments</h1>
#     <hr>
#     {% if yangilik.izohlar.exists %}
#                 {% for i in yangilik.izohlar.all %}

#                     <p>{{i.izoh}}</p>
#                     <span>{{i.user.username}} | {{i.created}}</span>
#                     <hr>
#                 {% endfor %}
#     {% else %}

#         <h2>Hozirda izohlar mavjud emas!</h2>
#     {% endif %}
    
    
    
#     </center>


#  izoh = form.cleaned_data['izoh'],
#              user = request.user,
#              news = news 
#             )
#          return redirect('one', news.id)



#  <!-- <a href="{% url 'create_category' %}">Tur yaratish</a> |  -->
#  <!-- <a href="{% url 'create_user' %}">user yartish</a> -->
#  |
#  <!-- <a href="{% url 'create_news' %}">news yartish</a>  -->
#  <!-- <button><a href="{% url 'login' %}">login</a></button>
#     {% if request.user.is_authenticated %}
#         <button><a href="{% url 'Logout' %}">log out</a></button>
#         <p>{{request.user.username}}</p>
#     {% endif %}   
#  |   -->
#  <br>
#         <!-- <form method="post" enctype="multipart/form-data">
#             {% csrf_token %}
#             {{form.as_p}}

#             <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
#                       <button class="btn btn-outline-success" type="submit">Search</button>
           
#         </form> -->
#             <!-- <center> -->


i=1
while i<6:
    print(i)
    i+=1