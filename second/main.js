import "./style.css"; //import of css styles
import * as THREE from "three";
import { Text } from "troika-three-text";
import grid from "./grid.svg";

// variables
let camera, scene, renderer;
let backPlaneGeo = new THREE.PlaneGeometry(60, 60, 8, 8);
let tileGeo = new THREE.PlaneGeometry(18, 18, 8, 8);
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

function possibleMoves(state_array) {
  // find the directions that are possible for the blank tile
  let possible_moves = [];
  let blank_tile = state_array.indexOf(0);
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

function applyMoves(state_array, move) {
  let new_state = state_array.slice();
  let blank_tile = state_array.indexOf(0);
  switch (move) {
    case "left":
      new_state[blank_tile] = new_state[blank_tile - 1];
      new_state[blank_tile - 1] = 0;
      break;
    case "right":
      new_state[blank_tile] = new_state[blank_tile + 1];
      new_state[blank_tile + 1] = 0;
      break;
    case "up":
      new_state[blank_tile] = new_state[blank_tile - 3];
      new_state[blank_tile - 3] = 0;
      break;
    case "down":
      new_state[blank_tile] = new_state[blank_tile + 3];
      new_state[blank_tile + 3] = 0;
      break;
  }
  return new_state;
}

function planeDrawer(xloc, yloc, state_array, parent_state) {
  let moves = possibleMoves(state_array);
  const backPlane = new THREE.Group();
  const backPlaneStart = new THREE.Mesh(
    backPlaneGeo,
    new THREE.MeshBasicMaterial({
      color: 0xffffff,
    })
  );
  backPlane.add(backPlaneStart);
  for (let i = 0; i < 9; i++) {
    const label = new Text();
    const tile = new THREE.Mesh(
      tileGeo,
      new THREE.MeshBasicMaterial({
        color: 0x00ff00,
      })
    );
    if (state_array[i] !== 0) {
      label.text = state_array[i];
      label.fontSize = 10;
      label.color = 0x000000;
      label.fontFace = "Arial";
      label.position.x = (i % 3) * 20 - 23;
      label.position.y = Math.floor(i / 3) * 20 - 15;
      label.position.z = 2;
    } else {
      tile.material.color.setHex(0xff0000);
    }
    tile.position.x = (i % 3) * 20 - 20;
    tile.position.y = Math.floor(i / 3) * 20 - 20;
    tile.position.z = 0;
    tile.name = i;
    backPlane.add(label, tile);
  }
  backPlane.position.x = xloc;
  backPlane.position.y = yloc;
  scene.add(backPlane);
  // state_array.sort(() => Math.random() - 0.5);

  if (yloc < 0) {
    console.log("TERMINATED");
  } else {
    for (let i = 0; i < moves.length; i++) {
      xloc += 100;
      const new_state = applyMoves(state_array, moves[i]);
      if (parent_state === new_state) console.log(new_state, parent_state);
      else {
        planeDrawer(xloc - 250, yloc - 80, new_state, state_array);
      }
    }
  }
}

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
