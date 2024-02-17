// Landing Screen.js
import React from 'react';
import { StyleSheet, View, Button, Image, Text } from 'react-native';

import {photo1} from './Camera1';
import {photo2} from './Camera2';
// var photo1 = undefined;
// var photo2 = undefined; 

const Landing = ({ navigation }) => {  
    const goToCamera1 = () => {
        navigation.navigate('Camera1');
    };

    const goToCamera2 = () => {
        navigation.navigate('Camera2');
    };

    const sendRequest = () => {
        console.log("yay, backend dumb");
    };

    if (photo1 === undefined && photo2 === undefined) {
        console.log("both null");
        return (
            <View style={styles.container}>
                <Text style={styles.header}>Welcome to Poke_CardTel</Text>
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
                        <Button title="Go to Camera1" onPress={goToCamera1} />
                    </View>
                </View>

                <View style={styles.itemContainer}>
                    <View style={styles.itemButton}>
                        <Button title="Go to Camera2" onPress={goToCamera2} />
                    </View>
                </View>
                <View style={styles.confirmContainer}>
                    <View style={styles.itemButton}>
                        <Button style={styles.confirmContainer} title="Confirm" onPress={sendRequest} />
                    </View>
                </View>
                <Text style={styles.footer}>Hi</Text>
            </View>
        );
    } else if (photo1 !== undefined && photo2 === undefined) {
        console.log("2 null");
        return (
            <View style={styles.container}>
                <Text style={styles.header}>Welcome to Poke_CardTel</Text>
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
                        <Button title="Go to Camera1" onPress={goToCamera1} />
                    </View>
                </View>

                <View style={styles.itemContainer}>
                    <View style={styles.itemButton}>
                        <Button title="Go to Camera2" onPress={goToCamera2} />
                    </View>
                </View>
                <View style={styles.confirmContainer}>
                    <View style={styles.itemButton}>
                        <Button style={styles.confirmContainer} title="Confirm" onPress={sendRequest} />
                    </View>
                </View>
                <Text style={styles.footer}>Hi</Text>
            </View>
        );
    } else if (photo1 === undefined && photo2 !== undefined) { 
        console.log("1 null");
        return (
            <View style={styles.container}>
                <Text style={styles.header}>Welcome to Poke_CardTel</Text>
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
                        <Button title="Go to Camera1" onPress={goToCamera1} />
                    </View>
                </View>

                <View style={styles.itemContainer}>
                    <View style={styles.itemButton}>
                        <Button title="Go to Camera2" onPress={goToCamera2} />
                    </View>
                </View>
                <View style={styles.confirmContainer}>
                    <View style={styles.itemButton}>
                        <Button style={styles.confirmContainer} title="Confirm" onPress={sendRequest} />
                    </View>
                </View>
                <Text style={styles.footer}>Hi</Text>
            </View>
        );
    } else {
        console.log("not null");
        return (
            <View style={styles.container}>
                <Text style={styles.header}>Welcome to Poke_CardTel</Text>
                <View style={styles.itemContainerPhoto}>
                    <Image style={styles.itemPhoto} source={{ uri: photo1.uri }} /> 
                </View>

                <View style={styles.itemContainerPhoto}>
                    <Image style={styles.itemPhoto} source={{ uri: photo2.uri }} />
                </View>

                <View style={styles.itemContainer}>
                    <View style={styles.itemButton}>
                        <Button title="Go to Camera1" onPress={goToCamera1} />
                    </View>
                </View>

                <View style={styles.itemContainer}>
                    <View style={styles.itemButton}>
                        <Button title="Go to Camera2" onPress={goToCamera2} />
                    </View>
                </View>
                <View style={styles.confirmContainer}>
                    <View style={styles.itemButton}>
                        <Button  title="Confirm" onPress={sendRequest} />
                    </View>
                </View>
                
            </View>
        );
    }
};

const styles = StyleSheet.create({
    header: {
        position: 'absolute',
        top: '2%',
        width: '100%',
        textAlign: 'center',
        fontSize: 24,
    },
    container: {
        flex: 1,
        height: '100%',
        flexDirection: 'row',
        flexWrap: 'wrap',
        alignContent: 'flex-start',
    },
    itemContainerPhoto: {
        width: '50%', 
        height: '50%',
    },
    itemContainer: {
        width: '50%', 
        height: '25%',
    },
    confirmContainer: {
        width: '100%', 
        height: '25%',
    },
    itemButton: {
        padding: 8,
        margin: 8,
        backgroundColor: '#EEEEEE',
    },
    itemPhoto: {
        padding: 8,
        margin: 8,
        backgroundColor: '#EEEEEE',
        top: '15%',
        width: '90%',
        aspectRatio: 3/4,
    },

    empty: {
        textAlign: 'center',
    },
  })

export default Landing;