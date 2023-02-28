const form = document.querySelector("#to-do-form");
const input = document.querySelector("#to-do-input");
const list = document.querySelector("#to-do-list");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  addToDo(input.value);
  input.value = "";
});

function addToDo(task) {
  const li = document.createElement("li");
  li.innerHTML = `<span>${task}</span><button>x</button>`;
  list.appendChild(li);
  li.querySelector("button").addEventListener("click", () => {
    li.remove();
  });
}
