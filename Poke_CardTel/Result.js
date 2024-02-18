import { StyleSheet, Text, View, Button, Image, ImageBackground } from 'react-native';

import background from './background.png';
import {response} from './Landing';
import {photo1, clearPhoto1} from './Camera1';
import {photo2, clearPhoto2} from './Camera2';

const Result = ({ navigation }) => {
  const sendRequest = () => {
    navigation.navigate('Landing');
    clearPhoto1();
    clearPhoto2();
  };

  return (
    <View style={styles.screen}>
        <ImageBackground source={background} resizeMode="cover" >        
            <View style={styles.container}>
                <View style={styles.itemContainerPhoto}>
                  <Image style={styles.itemPhoto} source={{ uri: photo1.uri }} />
                </View>

                <View style={styles.itemContainerPhoto}>
                  <Image style={styles.itemPhoto} source={{ uri: photo2.uri }} />
                </View>
                <View style={styles.gradeContainer}>
                  <Text style={styles.grade}> Grade: {response.data.grade}</Text>
                  <Text style={styles.grade}> Price: {response.data.price} </Text>
                </View>
                <View style={styles.confirmContainer}>
                    <View style={styles.itemButton}>
                        <Button  title="Scan a new card" onPress={sendRequest} />
                    </View>
                </View>
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
      height: '100%',
      flexDirection: 'row',
      flexWrap: 'wrap',
      alignContent: 'flex-start',
  },
  itemContainerPhoto: {
      width: '50%', 
      height: '40%',
  },
  itemPhoto: {
      padding: 8,
      margin: 8,
      top: '15%',
      width: '90%',
      aspectRatio: 3/4,
      backgroundColor: 'transparent',
      borderWidth: 4,
      borderColor: '#20232a',
  },

  gradeContainer: {
      width: '100%', 
      height: '25%',
  },
  grade: {
    marginTop: 16,
    paddingVertical: 8,
    backgroundColor: '#61dafb',
    color: '#20232a',
    textAlign: 'center',
    fontSize: 30,
    fontWeight: 'bold',
    backgroundColor: 'transparent',
    color: 'blue',
  },
  confirmContainer: {
    width: '100%', 
    height: '25%',
  },
  itemButton: {
      padding: 8,
      margin: 8,
      backgroundColor: 'transparent',
  },
})


export default Result;