import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView, Button, Image, ImageBackground } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera } from 'expo-camera';
import { shareAsync } from 'expo-sharing';
import { manipulateAsync } from 'expo-image-manipulator';
import * as MediaLibrary from 'expo-media-library';

import background from './background.png';

var photo2 = undefined;
const Camera2 = ({ navigation }) => {
  let cameraRef = useRef();
  const [hasCameraPermission, setHasCameraPermission] = useState();
  const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState();
  [photo2, setPhoto2] = useState();

  useEffect(() => {
    (async () => {
      const cameraPermission = await Camera.requestCameraPermissionsAsync();
      const mediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
      setHasCameraPermission(cameraPermission.status === "granted");
      setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
    })();
  }, []);

  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text>Permission for camera not granted. Please change this in settings.</Text>
  }

  let takePic = async () => {
    let options = {
      quality: 1,
      base64: true,
      exif: false
    };

    let newPhoto2 = await cameraRef.current.takePictureAsync(options);
    const scaledImage = await manipulateAsync(newPhoto2.uri, [], { compress: 0.5, base64: true});
    setPhoto2(scaledImage);
  };

  if (photo2) {
    let sharePic = () => {
      shareAsync(photo2.uri).then(() => {
        setPhoto2(undefined);
      });
    };
    
    return (
      <View style={styles.screen}>
        <ImageBackground style={styles.container} source={background} resizeMode="cover" >
            <View>
              <Image style={styles.preview} source={{ uri: photo2.uri }} />
            </View>
            
            <View style={styles.buttons}>  
              <Button  title="Share" onPress={sharePic} />
              {hasMediaLibraryPermission ? <Button title="Confirm" onPress={() => navigation.navigate('Landing', { photo2 })} /> : undefined}
              <Button title="Try Again" onPress={() => setPhoto2(undefined)} />
            </View>
        </ImageBackground>
      </View>


    );
  }

  return (
    <View style={styles.screen}>
      <ImageBackground style={styles.container} source={background} resizeMode="cover" >
        <Camera style={styles.camera} ref={cameraRef}>
          <StatusBar style="auto" />
        </Camera>
        <Text style={styles.warning}>
          Please scan the card with a DARK background!
        </Text>
        <View style={styles.buttonContainer}>
          <Button title="Take Pic" onPress={takePic} />
        </View>
      </ImageBackground>
    </View>

  );
}

const styles = StyleSheet.create({
  screen: {
    flex: 1,
  },
  container: {
    flex: 1,
    flexDirection: 'colomn',
    alignItems: "center", 
  },
  camera: {
    top: '10%',
    width: '90%',
    flexWrap: 'wrap',
    aspectRatio: 3/4,
  },
  warning: {
    color: 'white',
    top: '17%',
    fontSize: 16,
  },
  buttonContainer: {
    position: 'absolute',
    bottom: 20,
    alignSelf: 'center',
  },
  preview: {
    top: '10%',
    width: '90%',
    aspectRatio: 3/4,
  },
  buttons: {
    position: 'absolute',
    bottom: 20,
    alignSelf: 'center',
  }
});

export {photo2};
export function clearPhoto2() {
  photo2 = undefined;
}
export default Camera2;