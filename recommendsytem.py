movies = {
    "Star Wars": {"Jidnesh": 5, "Ayush": 4, "Vanssh": 3},
    "Avengers:EndGame": {"Jidnesh": 4, "Ayush": 5, "Vanssh": 4},
    "Top Gun:Maverick": {"Jidnesh": 5, "Ayush": 3, "Vanssh": 5},
    "Iron Man": {"Jidnesh": 5, "Ayush": 4, "Vanssh": 5}
}

def recommend_movies(user):
    recommendations = {}
    for movie, ratings in movies.items():
        for other_user, rating in ratings.items():
            if other_user != user:
                if other_user not in recommendations:
                    recommendations[other_user] = []
                recommendations[other_user].append((movie, rating))
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: sum(r[1] for r in x[1]), reverse=True)
    return sorted_recommendations

user = "Jidnesh"
recommended_users = recommend_movies(user)
if recommended_users:
    print(f"Recommended movies for {user} based on collaborative filtering:")
    for other_user, movies_rated in recommended_users:
        print(f"Movies recommended by {other_user}:")
        for movie, rating in movies_rated:
            print(f"- {movie}: {rating}")
else:
    print(f"No recommendations available for {user} based on collaborative filtering.")
