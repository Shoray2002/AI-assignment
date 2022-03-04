import "./style.css"; //import of css styles
import * as THREE from "three";
import grid from "./grid.svg";
import { backPlane } from "./backPlane.mjs";

// variables
let camera, scene, renderer;
let initial_state = [3, 1, 4, 2, 0, 6, 7, 8, 5];
init();

function init() {
  const texture = new THREE.TextureLoader().load(grid);
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(3, 3);
  camera = new THREE.PerspectiveCamera(
    18,
    window.innerWidth / window.innerHeight,
    1,
    10000
  );
  camera.position.set(0, 0, 1500);
  camera.lookAt(0, 0, 0);
  scene = new THREE.Scene();
  scene.background = texture;
  planeDrawer(0, 200, initial_state, null);

  // lights
  const ambientLight = new THREE.AmbientLight(0xffffff);
  scene.add(ambientLight);

  // renderer
  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  window.addEventListener("resize", onWindowResize);
  window.addEventListener("wheel", (event) => {
    // zoom in and out
    if (event.deltaY < 0) {
      camera.fov -= 2;
    } else {
      camera.fov += 2;
    }
    camera.updateProjectionMatrix();
    render();
  });
}

function possibleMoves(curr_state) {
  let possible_moves = [];
  let blank_tile = curr_state.indexOf(0);
  if (blank_tile % 3 !== 0) {
    possible_moves.push("left");
  }
  if (blank_tile % 3 !== 2) {
    possible_moves.push("right");
  }
  if (blank_tile > 2) {
    possible_moves.push("down");
  }
  if (blank_tile < 6) {
    possible_moves.push("up");
  }
  return possible_moves;
}

function applyMoves(curr_state, move) {
  let new_state = curr_state.slice();
  let blank_tile = new_state.indexOf(0);
  if (move === "left") {
    new_state[blank_tile] = new_state[blank_tile - 1];
    new_state[blank_tile - 1] = 0;
  } else if (move === "right") {
    new_state[blank_tile] = new_state[blank_tile + 1];
    new_state[blank_tile + 1] = 0;
  } else if (move === "down") {
    new_state[blank_tile] = new_state[blank_tile + 3];
    new_state[blank_tile + 3] = 0;
  } else if (move === "up") {
    new_state[blank_tile] = new_state[blank_tile - 3];
    new_state[blank_tile - 3] = 0;
  }
  return new_state;
}

function planeDrawer(xloc, yloc, state_array, parent_state) {
  let moves = possibleMoves(state_array);
  scene.add(backPlane(xloc, yloc, state_array, parent_state));
  console.log(moves);
  // if (moves.length > 0) {
  //   for (let i = 0; i < moves.length; i++) {
  //     let new_state = applyMoves(state_array, moves[i]);
  //     if (new_state.toString() !== parent_state.toString()) {
  //       planeDrawer(xloc, yloc, new_state, state_array);
  //     }
  //   }
  // }
}
// if (yloc < -50) {
//   console.log("TERMINATED");
// } else {
//   for (let i = 0; i < moves.length; i++) {
//     // xloc += 100;
//     const new_state = applyMoves(state_array, moves[i]);
//     if (JSON.stringify(new_state) === JSON.stringify(parent_state))
//       console.log(
//         "this is new state: " + new_state,
//         "this is parent state: " + parent_state
//       );
//     else {
//       planeDrawer(xloc - 250, yloc - 80, new_state, state_array);
//     }
//   }
// }
// }

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  render();
}

// render the scene
function render() {
  renderer.render(scene, camera);
}

// animate the scene
function animate() {
  requestAnimationFrame(animate);
  render();
}

animate();
