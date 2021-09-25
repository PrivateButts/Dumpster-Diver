import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { createBackground } from './vignette/three-vignette.js';

function initModelViewer() {
    const container = document.querySelector("#model-view")

    console.log(container.clientHeight)

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera( 75, container.clientWidth / container.clientHeight, 0.1, 1000 );

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize( container.clientWidth, container.clientHeight );
    container.appendChild( renderer.domElement );

    let IS_IOS = false;
    let vignette = createBackground({
        aspect: camera.aspect,
        grainScale: IS_IOS ? 0 : 0.001,
        colors: [0xffffff, 0xaaaaaa]
    });
    vignette.name = 'Vignette';
    vignette.renderOrder = -1;
    scene.add(vignette);


    const controls = new OrbitControls(camera, renderer.domElement);
    const loader = new GLTFLoader();

    loader.load( container.dataset.modelUrl, function ( gltf ) {

        scene.add( gltf.scene );

    }, undefined, function ( error ) {

        console.error( error );

    } );

    camera.position.z = 5;
    camera.position.y = 3;

    let hemiLight = new THREE.HemisphereLight( 0xffffff, 0x444444 );
    hemiLight.position.set( 0, 300, 0 );
    scene.add( hemiLight );

    let dirLight = new THREE.DirectionalLight( 0xffffff );
    dirLight.position.set( 75, 300, -75 );
    scene.add( dirLight );

    function animate() {
        requestAnimationFrame( animate );
        // cube.rotation.x += 0.01;
        // cube.rotation.y += 0.01;
        renderer.render( scene, camera );
    }
    animate();
}


document.addEventListener("DOMContentLoaded", initModelViewer);