# Encryption and Decryption Project

## Overview

This project provides tools for encrypting and decrypting text and text files using a custom encryption algorithm that utilizes a tree data structure. Our specific encryption and decryption method ensures secure and efficient data transformation.

## Features

- **Text Encryption**: Encrypts plain text input using our custom algorithm.
- **Text Decryption**: Decrypts the encrypted text back to its original form.
- **File Encryption**: Encrypts the contents of a text file.
- **File Decryption**: Decrypts the contents of an encrypted text file.
- **Custom Algorithm**: Utilizes a unique tree data structure for encryption and decryption processes.

## Algorithm Details

Our encryption and decryption algorithm is built around a custom tree data structure. Here’s a high-level overview of how it works:

### Encryption:

- The plain text is converted into a series of nodes.
- These nodes are organized into a binary tree structure based on specific rules.
- The traversal of the tree produces the encrypted text.

### Decryption:

- The encrypted text is used to rebuild the tree structure.
- The tree is traversed to retrieve the original plain text.
