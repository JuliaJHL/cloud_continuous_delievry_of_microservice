# IDS721Proj1-week1-2
# The final version of Project1 is in this repo (https://github.com/JuliaJHL/IDS721-Proj1-flask)


## project content
* Create a Guess Number game in Flask.
* Apply GitHub Actions as build system to deploy changes.
![actions](https://github.com/JuliaJHL/imgs_readme/blob/main/actions.png)
* Use IaC to deploy code on AWS (in week 3)

## project setup
1. Clone the repo:
```
git clone https://github.com/JuliaJHL/cloud_continuous_delievry_of_microservice.git
```
2. cd into the repo:
```
cd cloud_continuous_delievry_of_microservice
```
3. Create and source the virtual environment:
```
python3 -m venv env
source env/bin/activate
```
4. Install packages:
```
make install
```
5. Run flask locally
```
python app.py
```

## Examples
You will get this page after you run the `app.py`.
![login](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/login.png)
It will prompt invalid once you enter a integer over 100.
![invalid](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/valid.png)
You only have a total of 10 chances to guess the number. Wrong guesses, failures and successes will have corresponding pop-ups.
![big](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/too%20large.png)
![small](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/small.png)
![lose](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/lose.png)
![win](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/win.png)
