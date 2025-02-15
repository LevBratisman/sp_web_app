<template>
    <v-container class="bg-image">
      <div transition="fade-transition">
        <h1 class="introduce">
  
        </h1>
  
        <a href="https://t.me/simplephysics_polyteh" target=»_blank style="text-decoration: none;">
        <v-btn
          transition="slide-x-transition"
          size="large"
          height='72'
          variant="elevated"
          append-icon="mdi-send"
          color="white"
          rounded="xl"
          >
          Телеграм канал
        </v-btn>
        </a>
        <a href="https://t.me/simplephysicsbot" target=»_blank style="text-decoration: none;">
          <v-btn 
            transition="slide-x-transition"
            size="large"
            height='72'
            append-icon="mdi-robot"
            color="#1976D2"
            rounded="xl"
            variant="flat"
            block
            style="margin-right: 20px; margin-top: 20px;"
            >
            Телеграм бот
          </v-btn>
        </a>
        <a href="https://www.youtube.com/@Simplephysics-mpu" target=»_blank style="text-decoration: none;">
          <v-btn 
            transition="slide-x-transition"
            size="large"
            height='72'
            color="red"
            append-icon="mdi-youtube"
            rounded="xl"
            variant="flat"
            block
            style="margin-right: 20px; margin-top: 20px;"
            >
            YouTube
          </v-btn>
        </a>
        <a href="https://vk.com/simplephysicsmp" target=»_blank style="text-decoration: none;">
          <v-btn 
            transition="slide-x-transition"
            size="large"
            height='72'
            append-icon="mdi-account-multiple"
            color="#64B5F6"
            rounded="xl"
            variant="flat"
            block
            style="margin-right: 20px; margin-top: 20px;"
            >
            VK
          </v-btn>
        </a>
        <a href="#path" style="text-decoration: none;">
          <v-btn 
            transition="slide-x-transition"
            size="large"
            height='72'
            variant="tonal"
            append-icon="mdi-information"
            color="white"
            rounded="xl"
            block
            style="margin-right: 20px; margin-top: 20px;"
            >
            О нас
          </v-btn>
        </a>
        <div id="path"></div>
      </div>
      
    </v-container>
    <div class="introduce__content">
      <h1 style="margin-bottom: 40px;">
        SIMPLE PHYSICS
      </h1>
      <p style="margin-bottom: 15px;">
        Добро пожаловать! Перед вами проект Московского политехнического университета «Simple physics», 
        направленный на популяризацию физики среди широкой аудитории школьников и студентов. 
        Физика окружает нас повсюду и влияет на нашу повседневную жизнь. 
      </p>
      <p style="margin-bottom: 15px;">
        Мы уверены, что она намного интереснее, чем вы думаете, поэтому хотим показать вам это воочию. 
        Данная разработка включает в себя интерактивные уроки и видео, которые помогают учащимся лучше 
        понять и визуализировать сложные физические концепции. 
      </p>
      <p style="margin-bottom: 15px;">
        Проект «Simple physics» призван вдохновить людей на изучение науки, показать её увлекательную 
        сторону и дать возможность каждому увидеть, какую важную роль играет физика в нашем мире. 
        C нами вы полюбите физику, а она - откроется для вас совсем с другой стороны!
      </p>
    </div>
    <v-container style="color: #757474">
      <v-timeline side="start" style="text-align: left">
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Разработчик</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_9.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Разработчик</a>Лев</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Факультет информационных технологий
            </p>
            <p style="font-size: 17px;">
              Системная и программная инженерия
            </p>
            <p>
              231-3213
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Куратор</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_12.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Куратор</a>Светлана</div>
            <p style="font-size: 18px;">
              Ассистент Центра проектной деятельности
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Контент-мейкер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_2.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Контент-мейкер</a>Анастасия</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Факультет машиностроения
            </p>
            <p style="font-size: 17px;">
              Управление в технических системах
            </p>
            <p>
              231-251
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Дизайнер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_5.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Дизайнер</a>Василиса</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Полиграфический институт  
            </p>
            <p style="font-size: 17px;">
              Дизайн и технологии производства визуального контента
            </p>
            <p>
              231-722
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Дизайнер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия 2.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Дизайнер</a>Любовь</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
                      <p style="font-size: 18px;">
              Институт графики и искусства книги имени В.А. Фаворского
            </p>
            <p style="font-size: 17px;">
              Графический дизайн мультимедиа
            </p>
            <p>
              231-821
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Монтажер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_3.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Монтажер</a>Родион</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
                      <p style="font-size: 18px;">
              Факультет машиностроения
            </p>
            <p style="font-size: 17px;">
              Интеллектуальная электроника и промышленный интернет вещей
            </p>
            <p>
              231-262
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Контент-мейкер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_4.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Контент-мейкер</a>Ирина</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Полиграфический институт 
            </p>
            <p style="font-size: 17px;">
              Технология полиграфического и упаковочного производства
            </p>
            <p>
              231-721
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Участник</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_13.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Участник</a>Мерген</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Факультет химической технологии и биотехнологии
            </p>
            <p style="font-size: 17px;">
              Техносферная безопасность
            </p>
            <p>
              231-511
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Участник</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Участник</a>Артём</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Факультет машиностроения
            </p>
            <p style="font-size: 17px;">
              Управление в технических системах
            </p>
            <p>
              232-251
            </p>
          </div>
        </v-timeline-item>
  
              <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Контент-мейкер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_1.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Контент-мейкер</a>Оскар</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Факультет информационных технологий
            </p>
            <p style="font-size: 17px;">
              Системная и программная инженерия
            </p>
            <p>
              231-329
            </p>
          </div>
        </v-timeline-item>
  
              <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Контент-мейкер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_14.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Контент-мейкер</a>Ксения</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
                      <p style="font-size: 18px;">
              Институт издательского дела и журналистики
            </p>
            <p style="font-size: 17px;">
              Книгоиздательское дело
            </p>
            <p>
              231-013
            </p>
          </div>
        </v-timeline-item>
  
              <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Контент-мейкер</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Контент-мейкер</a>Оксана</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
                      <p style="font-size: 18px;">
              Институт издательского дела и журналистики
            </p>
            <p style="font-size: 17px;">
              Журналистика
            </p>
            <p>
              231-022
            </p>
          </div>
        </v-timeline-item>
  
              <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Участник</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_8.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Участник</a>Иван</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
                      <p style="font-size: 18px;">
              Факультет информационных технологий
            </p>
            <p style="font-size: 17px;">
              Информационные технологии управления бизнесом
            </p>
            <p>
              231-365
            </p>
          </div>
        </v-timeline-item>
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Участник</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_11.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Участник</a>Айдын</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
                      <p style="font-size: 18px;">
              Факультет информационных технологий
            </p>
            <p style="font-size: 17px;">
              Информационная безопасность
            </p>
            <p>
              231-352
            </p>
          </div>
        </v-timeline-item>	
  
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Участник</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_6.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Участник</a>Булат</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Факультет информационных технологий
            </p>
            <p style="font-size: 17px;">
              Веб-технологии
            </p>
            <p>
              231-023
            </p>
          </div>
        </v-timeline-item>
        
        <v-timeline-item>
          <template v-slot:opposite>
            <h2 class="role">Участник</h2>
          </template>
          <div>
            <v-img
              :width="300"
              aspect-ratio="16/9"
              cover
              src="/Монтажная область 1 копия_7.png"
            ></v-img>
          </div>
          <div style="margin-right: 10%;" class="bio">
            <div class="text-h6" style="margin-top: 30px;"><a class="role_small_size">Участник</a>Махрибан</div>
            <p style="font-size: 20px;">
              1 Курс
            </p>
            <p style="font-size: 18px;">
              Институт издательского дела и журналистики
            </p>
            <p style="font-size: 17px;">
              Журналистика
            </p>
            <p>
              231-023
            </p>
          </div>
        </v-timeline-item>
              
      </v-timeline>
    </v-container>
  </template>
  
  <script setup lang="ts">
  import Header from '../components/Header.vue'
  </script>
  
  <style scoped>
  
  .bio {
    width: 300px;
  }
  
  .v-timeline-item__body {
    max-width: 500px;
    padding: 0;
  }
  .role{
    display: block;
  }
  .role_small_size{
    display: none;
    font-size: 25px;
  }
  .bg-image {
      height: 100vh;
      min-width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
      background: 
        linear-gradient(rgba(0,0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
        url(/back_ground.jpg);
      background-size: cover;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-position: top; 
  }
  
  .mascot {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  
  
  .introduce {
    text-align: center;
    opacity: 1;
    font-size: 50px;
  }
  
  .introduce__content {
    text-align: center;
    margin: 50px 65px;
    color:#828181;
  }
  
  .introduce__btn {
    display: block;
  }
  
  @media (max-width: 1024px) {
    .bg-image {
        background: 
        linear-gradient(rgba(0,0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
        url(/background_tabletsize.jpeg);
      }
  }
  
  @media (max-width: 601px) {
      .role{
        display: none;
      }
      .role_small_size{
        display: block;
      }
      .introduce__content {
        margin-left: 35px;
        margin-right: 35px;
      }
    }
  
    @media (max-width: 450px) {
      .bg-image {
        background: 
        linear-gradient(rgba(0,0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
        url(/background_smallsize.jpeg);
      }
    }
  
    @media (max-width: 360px) {
      .bio {
        width: 250px;
      }
  
      .bg-image {
        background: 
        linear-gradient(rgba(0,0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
        url(/background_smallsize.jpeg);
      }
    }
  
    @media (max-width: 320px) {
      .bio {
        width: 200px;
      }
    }
  
  </style>
  