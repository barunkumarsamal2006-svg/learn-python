user_age_string='17' 
has_parental_consent=True

user_age=int(user_age_string)

is_adult =user_age>=18


can_use_ai= is_adult or has_parental_consent


print('verification for usrer account')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
print(f'Has consent :{can_use_ai}')
print(f'User age:{user_age}')
print(f'Is adult :{is_adult}')
print(f'Access granted :{can_use_ai}')