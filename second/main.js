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
  scene.add(planeDrawer(200));

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

function planeDrawer(yloc) {
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
    if (initial_state[i] !== 0) {
      label.text = initial_state[i];
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
  backPlane.position.y = yloc;
  return backPlane;
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
