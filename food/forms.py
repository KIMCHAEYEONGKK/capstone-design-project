from django import forms
from food.models import Food, Food_morning, Food_lunch, Food_dinner,Calorie

class FoodForm(forms.Form):
    food_calorie = forms.CharField(max_length=5, label="음식 칼로리", required=True)
    food_name = forms.CharField(max_length=20, label="음식 이름", required=True)

    class Meta:
        model = Food
        fields = ['food_calorie','food_name']



class CalorieForm(forms.Form):
    health_calorie = forms.CharField(max_length=5, label="소비한 칼로리", required=True)
    # eat_calorie_morning = forms.CharField(max_length=5, label="아침에 섭취 칼로리", required=True)
    # eat_calorie_lunch = forms.CharField(max_length=5, label="'점심에 섭취 칼로리", required=True)
    # eat_calorie_dinner = forms.CharField(max_length=5, label="저녁에 섭취 칼로리", required=True)

    class Meta:
        model = Calorie
        field = ['health_calorie',]




class MorningForm(forms.Form):
    name = forms.CharField(max_length=20, label="아침음식이름", required=True)
    calorie = forms.CharField(max_length=5, label="아침음식 칼로리", required=True)

    field_orders=['m_name',"m_calorie"]


    class Meta:
        model = Food_morning
        fields = ['name','calorie']
        exclude = ('user')



class LunchForm(forms.Form):
    name = forms.CharField(max_length=20, label="점심음식이름", required=True)
    calorie = forms.CharField(max_length=5, label="점심음식칼로리", required=True)

    class Meta:
        model = Food_lunch
        fields = ['name','calorie']
        exclude = ('user')



class DinnerForm(forms.Form):
    name = forms.CharField(max_length=20, label="저녁음식이름", required=True)
    calorie = forms.CharField(max_length=5, label="저녁음식 칼로리", required=True)

    class Meta:
        model = Food_dinner
        fields = ['name','calorie']
        exclude = ('user')

