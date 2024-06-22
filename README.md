
---

<!-- Banner -->

# EduCollab

EduCollab is a common platform for students and faculty to upload and share files, including all sorts of study material, accessible to all registered members.

### Goal

To create a secure and scalable platform for both college students and faculty to easily share coursework-related resources, reducing dependency on social media platforms. In the future, the platform can also serve as an e-library for college students.

### Tech Stack

- **Frontend**: HTML, CSS, and JavaScript
- **Backend**: Python with the [Django](https://docs.djangoproject.com/en/3.1/) Framework

Hit [:star2:](#) to show some :heart:!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Development Environment Setup: Windows

<details>
<summary>Step 1: Downloading and Installing the Code Editor</summary>
<br>
You can install any one of the following code editors:
<ul>
<li><a href="https://code.visualstudio.com/">Visual Studio Code</a></li>
<li><a href="https://www.sublimetext.com/3">Sublime Text 3</a></li>
<li><a href="https://atom.io/">Atom</a></li>
</ul>
</details>

---

<details>
<summary>Step 2: Installing Python 3.7</summary>
<br>
Download <a href="https://www.python.org/downloads/">Python 3.7 or higher</a>
<ul>
<li>Download the Windows x86-64 executable installer for the 64-bit version of Windows</li>
<li>Download the Windows x86 executable installer for the 32-bit version of Windows</li>
<li>Make sure to check '<b>Add Python 3.7 to Path</b>' in the setup window of the installer</li>
</ul>
Verify the installation from the command prompt (Terminal) using the following command:
<br>

```bash
python --version
```

The installed version of Python will be printed.
</details>

---

<details>
<summary>Step 3: Installing Git</summary>
<br>
Download <a href="https://git-scm.com/downloads">Git</a>.
</details>

---

<details>
<summary>Step 4: Fork the Repository</summary>
<br>
Click on  a href="#" target="_self"><img src="https://user-images.githubusercontent.com/63921263/110382285-b07bba80-8080-11eb-8407-d354849c1753.png" width="16"></img></a> to fork <a href="https://github.com/mxbb-0-1/Edu-Collab">this repository</a>.
</details>

---

<details>
<summary>Step 5: Creating Project Directory</summary>
<br>
Note: We're creating the project directory on the desktop for easy and fast access.

```bash
cd desktop
mkdir Projects
cd Projects
```
</details>

---

<details>
<summary>Step 6: Cloning Repository using Git</summary>
<br>

```bash
git clone https://github.com/<your-github-username>/EduCollab.git
```
</details>

---

<details>
<summary>Step 7: Change Directory to EduCollab</summary>
<br>

```bash
cd EduCollab
```
</details>

---

<details>
<summary>Step 8: Add a Reference to the Original Repository</summary>
<br>

```bash
git remote add upstream https://github.com/mxbb-0-1/Edu-Collab
```
</details>

---

<details>
<summary>Step 9: Creating Virtual Environment</summary>
<br>
Install virtualenv:

```bash
pip install virtualenv
```

Creating a Virtual Environment named `myvenv`:

```bash
virtualenv myvenv -p python3.7
```

To activate `myvenv`:

```bash
myvenv\Scripts\activate
```

To deactivate `myvenv`:

```bash
deactivate
```
</details>

---

<details>
<summary>Step 10: Installing Requirements</summary>
<br>
Note: Before installing requirements, ensure the virtual environment is activated.

```bash
pip install -r requirements.txt
```
</details>

---

<details>
<summary>Step 11: Making Database Migrations</summary>
<br>

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

---

<details>
<summary>Step 12: Creating Superuser to Access Admin Panel</summary>
<br>

```bash
python manage.py createsuperuser
```
</details>

---

<details>
<summary>Step 13: Running the Project on Local Server</summary>
<br>
Note: Before running the project on a local server, ensure the virtual environment is activated.

```bash
python manage.py runserver
```
</details>

---

## Congratulations on setting up the project locally!

---

## Contributing

We welcome contributions to improve this project! Here’s how you can help:

1. **Fork the repository**
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m "Add feature/your-feature-name"
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a pull request** detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out:

- **GitHub**: [mxbb-0-1](https://github.com/mxbb-0-1)
- **Email**: [asblueberry43@gmail.com](mailto:asblueberry43@gmail.com)

---

