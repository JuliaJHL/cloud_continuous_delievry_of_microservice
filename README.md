# IDS721Proj1-cloud_continuous_delievry_of_microservice
## project content
* Create a Guess Number game in Flask.
* Apply GitHub Actions as build system to deploy changes.
![actions](https://github.com/JuliaJHL/imgs_readme/blob/main/actions.png)
* Use IaC to deploy code on AWS Cloud9 (also tried AWS Elastic BeansTalk).
![cloud9](https://github.com/JuliaJHL/imgs_readme/blob/main/cloud9.png)
![one](https://github.com/JuliaJHL/imgs_readme/blob/main/one.png)
![benas](https://github.com/JuliaJHL/imgs_readme/blob/main/beans.png)
![all](https://github.com/JuliaJHL/imgs_readme/blob/main/all.png)

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
You will get the login page after you run the `app.py`.
![login](https://github.com/JuliaJHL/imgs_readme/blob/main/enter.png)
The username is `IDS721` and the password is `DUKE2023`. You will receive a successful login after entering the correct username and password. Otherwise, you will receive a login failure.
![success](https://github.com/JuliaJHL/imgs_readme/blob/main/success.png)
![fail](https://github.com/JuliaJHL/imgs_readme/blob/main/fail.png)
