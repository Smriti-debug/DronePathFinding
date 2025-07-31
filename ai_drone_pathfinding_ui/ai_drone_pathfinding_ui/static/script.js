const gridSize = 10;
let gridData = Array.from({ length: gridSize }, () => Array(gridSize).fill(""));
let start = null, goal = null;

const gridDiv = document.getElementById('grid');
function createGrid() {
  gridDiv.innerHTML = '';
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      const cell = document.createElement('div');
      cell.className = 'cell';
      cell.dataset.row = i;
      cell.dataset.col = j;
      cell.onclick = () => handleCellClick(i, j, cell);
      gridDiv.appendChild(cell);
    }
  }
}

function handleCellClick(i, j, cell) {
  if (!start) {
    start = [i, j];
    gridData[i][j] = 'S';
    cell.classList.add('start');
  } else if (!goal && gridData[i][j] === "") {
    goal = [i, j];
    gridData[i][j] = 'G';
    cell.classList.add('goal');
  } else if (gridData[i][j] === "") {
    gridData[i][j] = 'X';
    cell.classList.add('obstacle');
  }
}

function resetGrid() {
  start = null;
  goal = null;
  gridData = Array.from({ length: gridSize }, () => Array(gridSize).fill(""));
  createGrid();
}

async function findPath() {
  if (!start || !goal) {
    alert("Set both start and goal positions.");
    return;
  }
  const algorithm = document.getElementById("algorithm").value;
  const res = await fetch('/find_path', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grid: gridData, start, goal, algorithm })
  });
  const data = await res.json();
  const path = data.path;

  for (let [i, j] of path) {
    if ((i === start[0] && j === start[1]) || (i === goal[0] && j === goal[1])) continue;
    const index = i * gridSize + j;
    gridDiv.children[index].classList.add('path');
  }
}

createGrid();
