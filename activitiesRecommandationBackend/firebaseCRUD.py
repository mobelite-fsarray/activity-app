# Create a new document in Firestore
def create_document(collection, document_data):
    db = firestore.client()
    doc_ref = db.collection(collection).document()
    document_data.update({'id': doc_ref.id})
    doc_ref.set(document_data)
    print('Document created with ID:', doc_ref.id)
    return doc_ref.id


# Delete a new document in Firestore
def delete_document(collection, id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(id)
    print('Document deleted with ID:', doc_ref.id)
    doc_ref.delete(document_data)