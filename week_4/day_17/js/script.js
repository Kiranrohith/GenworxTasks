const navItems = [
    {
        name: "Home",
        link: "#home"
    },
    {
        name: "About",
        link: "#about"
    },
    {
        name: "Skills",
        link: "#skills"
    },
    {
        name: "Experience",
        link: "#experience"
    },
    {
        name: "Projects",
        link: "#projects"
    },
    {
        name: "Contact",
        link: "#contact"
    }
];

const defaultSkills = [
    {
        id: 1,
        name: "Python",
        icon: "devicon-python-plain colored",
        className: "skill-card"
    },
    {
        id: 2,
        name: "FastAPI",
        icon: "devicon-fastapi-plain colored",
        className: "skill-card"
    },
    {
        id: 3,
        name: "PostgreSQL",
        icon: "devicon-postgresql-plain colored",
        className: "skill-card"
    },
    {
        id: 4,
        name: "MySQL",
        icon: "devicon-mysql-plain colored",
        className: "skill-card"
    },
    {
        id: 5,
        name: "Java",
        icon: "devicon-java-plain colored",
        className: "skill-card"
    },
    {
        id: 6,
        name: "HTML5",
        icon: "devicon-html5-plain colored",
        className: "skill-card"
    },
    {
        id: 7,
        name: "CSS3",
        icon: "devicon-css3-plain colored",
        className: "skill-card"
    },
    {
        id: 8,
        name: "Git",
        icon: "devicon-git-plain colored",
        className: "skill-card"
    },
    {
        id: 9,
        name: "GitHub",
        icon: "devicon-github-original colored",
        className: "skill-card"
    },
    {
        id: 10,
        name: "SQL",
        icon: "fa-solid fa-database",
        className: "skill-card"
    },
    {
        id: 11,
        name: "REST API",
        icon: "fa-solid fa-server",
        className: "skill-card"
    },
    {
        id: 12,
        name: "VS Code",
        icon: "devicon-vscode-plain colored",
        className: "skill-card"
    }
];

let skills = loadSkillsFromStorage();

function loadSkillsFromStorage() {
    const stored = localStorage.getItem("skills");
    return stored ? JSON.parse(stored) : defaultSkills;
}

function saveSkillsToStorage() {
    localStorage.setItem("skills", JSON.stringify(skills));
}

function renderNavbar() {
    const navbar = document.getElementById("navbar");

    navItems.forEach(item => {
        const link = document.createElement("a");
        link.textContent = item.name;
        link.href = item.link;

        navbar.appendChild(link);
    });
}

function renderSkills() {
    const skillList = document.getElementById("skills-list");
    skillList.innerHTML = "";

    skills.forEach(skill => {
        const card = document.createElement("div");
        card.className = skill.className;
        card.setAttribute("data-id", skill.id);

        const icon = document.createElement("i");
        icon.className = skill.icon;

        const title = document.createElement("h3");
        title.textContent = skill.name;

        card.appendChild(icon);
        card.appendChild(title);

        skillList.appendChild(card);
    });
}

// Add Skill Modal Functions
const modal = document.getElementById("skill-modal");
const addSkillBtn = document.getElementById("add-skill-btn");
const closeModalBtn = document.getElementById("close-modal");
const cancelBtn = document.getElementById("cancel-btn");
const addSkillForm = document.getElementById("add-skill-form");
const skillNameInput = document.getElementById("skill-name");
const skillIconInput = document.getElementById("skill-icon");

function openModal() {
    modal.classList.add("active");
    skillNameInput.focus();
}

function closeModal() {
    modal.classList.remove("active");
    addSkillForm.reset();
}

function addNewSkill(e) {
    e.preventDefault();
    
    const skillName = skillNameInput.value.trim();
    const skillIcon = skillIconInput.value.trim() || "fa-solid fa-star";
    
    if (!skillName) {
        alert("Skill name is required!");
        return;
    }
    
    const newSkill = {
        id: Math.max(...skills.map(s => s.id), 0) + 1,
        name: skillName,
        icon: skillIcon,
        className: "skill-card"
    };
    
    skills.push(newSkill);
    saveSkillsToStorage();
    renderSkills();
    closeModal();
}

addSkillBtn.addEventListener("click", openModal);
closeModalBtn.addEventListener("click", closeModal);
cancelBtn.addEventListener("click", closeModal);
addSkillForm.addEventListener("submit", addNewSkill);

window.addEventListener("click", (e) => {
    if (e.target === modal) {
        closeModal();
    }
});

// Theme Toggle

const themeBtn = document.getElementById("theme-btn");

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if(document.body.classList.contains("dark")){

        themeBtn.textContent = "☀️";

    }else{

        themeBtn.textContent = "🌙";

    }

});

const quoteBtn = document.getElementById("quote-btn");
const quoteText = document.getElementById("quote-text");

quoteBtn.addEventListener("click", loadQuote);

async function loadQuote(){

    try{

        const response = await fetch("https://dummyjson.com/quotes/random");

        const data = await response.json();
        console.log(data);

        quoteText.textContent = `"${data.quote}" — ${data.author}`;

    }

    catch(error){

        quoteText.textContent = "Failed to load quote.";

    }

}
renderNavbar();
renderSkills();
