// Landing Screen.js
import React from 'react';
import { StyleSheet, View, Button, Image, Text, TextInput, ImageBackground, Keyboard } from 'react-native';
import axios from 'axios';
import { useState } from 'react';


import {photo1} from './Camera1';
import {photo2} from './Camera2';

import background from './background.png';

var response = "";
const Landing = ({ navigation }) => {  
    const goToCamera1 = () => {
        navigation.navigate('Camera1');
    };

    const goToCamera2 = () => {
        navigation.navigate('Camera2');
    };

    const sendRequest = async () => {
        if (cardName === '') {
            alert('Please enter the card name.');
        } else {
            try {
                
                //const url = 'http://100.112.90.138:5000/';
                const url = 'http://142.1.200.8:5000/';
                const data = {"name": cardName, "Photo1": photo1.base64, "Photo2": photo2.base64};
                console.log("called");
                response = await axios.post(url, data);
                console.log("called1");
            } catch (error) {
                console.error('Error fetching menu:', error);
                throw error; // Rethrow the error to handle it where the function is called
            }
            navigation.navigate('Result', { response });
        }
    };
    
    const [cardName, setCardName] = useState('');
    const handleInputChange = (text) => {
        setCardName(text);
    };
    

    if (photo1 === undefined && photo2 === undefined) {
        return (
            <View style={styles.screen}>
                <ImageBackground source={background} resizeMode="cover" >
                    <View style={styles.headerContainer}>
                        <Text style={styles.header}>Welcome to PokeCardtel</Text>
                    </View>
                
                    <View style={styles.container}>
                        <View style={styles.itemContainerPhoto}>
                            <View style={styles.itemPhoto}> 
                                <Text style = {styles.empty}>
                                    Take a picture
                                </Text>
                            </View>
                        </View>

                        <View style={styles.itemContainerPhoto}>
                            <View style={styles.itemPhoto}> 
                                <Text style = {styles.empty}>
                                    Take a picture
                                </Text>
                            </View>
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo1" onPress={goToCamera1} />
                            </View>
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo2" onPress={goToCamera2} />
                            </View>
                        </View>
                    </View>
                </ImageBackground>
            </View>
        );
    } else if (photo1 !== undefined && photo2 === undefined) {
        return (
            <View style={styles.screen}>
                <ImageBackground source={background} resizeMode="cover" >
                    <View style={styles.headerContainer}>
                        <Text style={styles.header}>Welcome to PokeCardtel</Text>
                    </View>
                
                    <View style={styles.container}>
                        <View style={styles.itemContainerPhoto}>
                            <Image style={styles.itemPhoto} source={{ uri: photo1.uri }} />
                        </View>

                        <View style={styles.itemContainerPhoto}>
                            <View style={styles.itemPhoto}> 
                                <Text style = {styles.empty}>
                                    Take a picture
                                </Text>
                            </View>
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo1" onPress={goToCamera1} />
                            </View>
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo2" onPress={goToCamera2} />
                            </View>
                        </View>
                    </View>
                </ImageBackground>
            </View>
        );
    } else if (photo1 === undefined && photo2 !== undefined) { 
        return (
            <View style={styles.screen}>
                <ImageBackground source={background} resizeMode="cover" >
                    <View style={styles.headerContainer}>
                        <Text style={styles.header}>Welcome to PokeCardtel</Text>
                    </View>
                
                    <View style={styles.container}>
                        <View style={styles.itemContainerPhoto}>
                            <View style={styles.itemPhoto}> 
                                <Text style = {styles.empty}>
                                    Take a picture
                                </Text>
                            </View>
                        </View>

                        <View style={styles.itemContainerPhoto}>
                            <Image style={styles.itemPhoto} source={{ uri: photo2.uri }} />
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo1" onPress={goToCamera1} />
                            </View>
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo2" onPress={goToCamera2} />
                            </View>
                        </View>
                    </View>
                </ImageBackground>
            </View>
        );
    } else {
        return (
            <View style={styles.screen}>
                <ImageBackground source={background} resizeMode="cover" >
                    <View style={styles.headerContainer}>
                        <Text style={styles.header}>Welcome to PokeCardtel</Text>
                    </View>
                
                    <View style={styles.container}>
                        <View style={styles.itemContainerPhoto}>
                            <Image style={styles.itemPhoto} source={{ uri: photo1.uri }} />
                        </View>

                        <View style={styles.itemContainerPhoto}>
                            <Image style={styles.itemPhoto} source={{ uri: photo2.uri }} />
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo1" onPress={goToCamera1} />
                            </View>
                        </View>

                        <View style={styles.itemContainer}>
                            <View style={styles.itemButton}>
                                <Button title="Take Photo2" onPress={goToCamera2} />
                            </View>
                        </View>
                        <View style={styles.confirmContainer}>
                            <View style={styles.textInput}>
                                <TextInput
                                    style={styles.input}
                                    placeholder="Please enter the card name…"
                                    onChangeText={handleInputChange} // Update state when text changes
                                    value={cardName} // Set input value to state variable
                                    onSubmitEditing={Keyboard.dismiss}
                                />
                            </View>
                            <View style={styles.itemButton}>
                                <Button  title="Confirm" onPress={sendRequest} />
                            </View>
                        </View>
                    </View>
                </ImageBackground>
            </View>
        );
    }
};

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
    headerContainer: {
        padding: 12,
    },
    header: {
        // position: 'absolute',
        marginTop: 16,
        paddingVertical: 8,
        borderWidth: 4,
        borderColor: '#20232a',
        borderRadius: 6,
        backgroundColor: '#61dafb',
        color: '#20232a',
        textAlign: 'center',
        fontSize: 30,
        fontWeight: 'bold',
        backgroundColor: 'transparent',
        color: 'white',
    },
    itemContainerPhoto: {
        width: '50%', 
        height: '40%',
    },
    itemContainer: {
        width: '50%', 
        height: '10%',
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

    empty: {
        textAlign: 'center',
        color: 'white',
    },
    input: {
        padding: 8,
        borderWidth: 2,
        borderRadius: 4,
    },
    textInput: {
        padding: 8,
        margin: 8,
        backgroundColor: 'transparent',
        textAlign: 'center', 
        backgroundColor: 'transparent',
    },
  })

export {response};
export default Landing;