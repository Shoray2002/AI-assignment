import * as THREE from "three";
import { Text } from "troika-three-text";

let backPlaneGeo = new THREE.PlaneGeometry(60, 60, 8, 8);
let tileGeo = new THREE.PlaneGeometry(18, 18, 8, 8);

function backPlane(xloc, yloc, state_array) {
  const backPlane = new THREE.Group();
  // const backPlaneBase = new THREE.Mesh(
  //   backPlaneGeo,
  //   new THREE.MeshBasicMaterial({
  //     color: 0xffffff,
  //   })
  // );
  // backPlane.add(backPlaneBase);
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

  backPlane.position.x = xloc * 1.2;
  backPlane.position.y = yloc * 1.2;

  return backPlane;
}

export { backPlane };
